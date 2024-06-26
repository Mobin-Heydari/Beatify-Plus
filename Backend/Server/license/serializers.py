from rest_framework import serializers

from .models import BeatLicense, License, LicenseFile

from beats.models import Beat




class LicenseFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LicenseFile
        fields = ('file_name', 'file', 'id')
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['file_name'] = instance.file.name
        return representation




class LicenseSerializer(serializers.ModelSerializer):
    
    license_files = LicenseFileSerializer(many=True, read_only=True)
    
    class Meta:
        model = License
        fields = '__all__'
        
    def get_license_files(self, obj):
        license_files = LicenseFile.objects.filter(license_model_id=obj.id)
        return list(license_files)
        


class BeatLicenseSerializer(serializers.ModelSerializer):
    
    licenses = LicenseSerializer(many=True)
    class Meta:
        model = BeatLicense
        fields = '__all__'
        