from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import *

from . import serializers
from .models import BeatLicense, License, LicenseFile
from .permissions import IsBeatLicenseOwnerOrForbidden

from beats.models import Beat



class BeatLicenses(APIView):
    def get(self, request, slug):
        queryset = Beat.objects.get(slug=slug)
        instance = get_object_or_404(BeatLicense, beat=queryset)
        serializer = serializers.BeatLicenseSerializer(instance=instance)
        return Response(serializer.data, status=HTTP_200_OK)
    


class LicenseViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated, IsBeatLicenseOwnerOrForbidden]
    
    def create(self, request, slug):
        
        beat = get_object_or_404(Beat, slug=slug)
        
        serializer = serializers.LicenseSerializer(data=request.data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    'Detail':{
                        'Massage' : 'Created.',
                        'data' : serializer.data
                    }
                },
                status=HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'Detail':{
                        'Massage' : 'Error.',
                        'Errors' : serializer.errors
                    }
                },
                status=HTTP_400_BAD_REQUEST
            )