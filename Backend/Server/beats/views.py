from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from . import serializers
from .models import Beat, BeatInformation
from .paginations import BeatPagination
from .permissions import IsOwnerOrReadOnly





class BeatViewSet(ViewSet, BeatPagination):
    """
    ViewSet for Beats
    """
    # Define the permission classes for this viewset
    permission_classes = [IsOwnerOrReadOnly]

    def list(self, request):
        """
        List all beats
        """
        # Get all beats and order them by creation date (newest first)
        queryset = Beat.objects.all().order_by('-created')
        
        # Paginate the queryset using the BeatPagination class
        result = self.paginate_queryset(queryset, request)
        
        # Serialize the paginated result using the BeatSerializer
        serializer = serializers.BeatSerializer(result, many=True)
        
        # Return the paginated response
        return self.get_paginated_response(serializer.data)


    def retrieve(self, request, pk):
        """
        Retrieve a single beat by slug (pk)
        """
        # Get the beat instance by slug (pk)
        query = get_object_or_404(Beat, slug=pk)
        
        # Check if the beat is published or the requesting user is the owner
        if query.published_status == 'Published' or query.owner == request.user:
            # Serialize the beat instance using the BeatSerializer
            serializer = serializers.BeatSerializer(instance=query)
            
            # Return the serialized data with a 200 OK status
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return a 403 Forbidden response if the beat is not published or the user doesn't have access
            return Response(
                {
                    'Detail' : 'The beat is not published or you dont have the access to read'
                },
                status=status.HTTP_403_FORBIDDEN
            )


    def create(self, request):
        """
        Create a new beat
        """
        # Check if the requesting user is authenticated
        if request.user.is_authenticated:
            user = request.user
            
            # Check if the user is a Producer or Musician type
            if user.user_type == 'PRD':
                # Create a new beat instance using the BeatSerializer
                serializer = serializers.BeatSerializer(data=request.data, context={'request': request})
                
                # If the data is valid, save the instance and return a 201 Created response
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        {
                            'Detail':'Created.'
                        },
                         status=status.HTTP_201_CREATED
                    )
                else:
                    # Return a 400 Bad Request response if the data is invalid
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return a 400 Bad Request response if the user type is invalid
                return Response(
                    {
                        'Detail':'invalid user type.'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # Return a 401 Unauthorized response if the user is not authenticated
            return Response(
                {
                    'Detail':'Unauthorized user.'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )


    def update(self, request, pk):
        """
        Update a beat
        """
        # Get the beat instance by slug (pk)
        queryset = get_object_or_404(Beat, slug=pk)
        
        # Check if the requesting user is authenticated
        if request.user.is_authenticated:
            # Check object permissions using the permission classes
            self.check_object_permissions(request, queryset)
            
            # Update the beat instance using the BeatSerializer
            serializer = serializers.BeatSerializer(queryset, data=request.data, partial=True)
            
            # If the data is valid, update the instance and return a 200 OK response
            if serializer.is_valid(raise_exception=True):
                
                serializer.update(instance=queryset, validated_data=serializer.validated_data)
                
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
            else:
                # Return a 400 Bad Request response if the data is invalid
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # Return a 401 Unauthorized response if the user is not authenticated
            return Response(
                {
                    'Detail':'you are not authenticated.'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )