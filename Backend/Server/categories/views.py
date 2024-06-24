from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView, Response
from rest_framework.status import *

from . import serializers
from .models import Category
from .paginations import CategoryPagination




class CategoryViewSet(ViewSet, CategoryPagination):
    
    def list(self, request):
        queryset = Category.objects.all()
        result = self.paginate_queryset(queryset, request)
        serializer = serializers.CategorySerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)
    

    def retrieve(self, request, pk):
        query = get_object_or_404(Category, slug=pk)
        serializer = serializers.CategorySerializer(instance=query)
        return Response(serializer.data, status=HTTP_200_OK)
    