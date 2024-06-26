from rest_framework import serializers

from .models import BeatLicense, License, LicenseFile

from beats.models import Beat






class LicenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = License
        fields = '__all__'
        



class LicenseFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LicenseFile
        fields = '__all__'
        



class BeatLicenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeatLicense
        fields = '__all__'
        