from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from . import serializers
from .models import Beat, BeatInformation
from .paginations import BeatPagination





class BeatViewSet(ViewSet, BeatPagination):
    
    def list(self, request):
        queryset = Beat.objects.all().order_by('-created')
        result = self.paginate_queryset(queryset, request)
        serializer = serializers.BeatSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
        
    
    def retrieve(self, request, pk):
        query = get_object_or_404(Beat, slug=pk)
        if query.published_status == 'Published' or query.owner == request.user:
            serializer = serializers.BeatSerializer(instance=query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    'Detail' : 'The beat is not published or you dont have the access to read'
                },
                status=status.HTTP_403_FORBIDDEN
            )       
    
    def create(self, request):
        if request.user.is_authenticated == True:
            user = request.user
            # Then we will check that this user is the Producer user or Musician user or not?
            if user.type == 'PRD' or user.type == 'MUC':
                # If yes then we will go forward
                serializer = serializers.BeatSerializer(data=request.data)
                # If the data is valid then save the data into database else give errors
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"Response":"Created."}, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error":"invalid user type."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"Unauthorized user."},status=status.HTTP_401_UNAUTHORIZED)