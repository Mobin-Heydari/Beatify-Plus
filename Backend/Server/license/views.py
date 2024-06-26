from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework.status import *

from . import serializers
from .models import BeatLicense, License, LicenseFile

from beats.models import Beat



class BeatLicenses(APIView):
    def get(self, request, slug):
        queryset = Beat.objects.get(slug=slug)
        instance = get_object_or_404(BeatLicense, beat=queryset)
        serializer = serializers.BeatLicenseSerializer(instance=instance)
        return Response(serializer.data, status=HTTP_200_OK)