from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView, Response
from rest_framework.status import *

from . import serializers
from .models import Mood
from .paginations import MoodPagination




class MoodViewSet(ViewSet, MoodPagination):
    
    def list(self, request):
        queryset = Mood.objects.all()
        result = self.paginate_queryset(queryset, request)
        serializer = serializers.MoodSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)
    

    def retrieve(self, request, pk):
        query = get_object_or_404(Mood, slug=pk)
        serializer = serializers.MoodSerializer(instance=query)
        return Response(serializer.data, status=HTTP_200_OK)
    