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
    
    def create(self, validated_data):
        
        beat = self.context['beat']
        
        vd =validated_data
        
        _license = License.objects.create(
            title = vd['title'],
            price = vd['price'],
            description = cd['description']
        )
        
        _license.save()
        
        beat_license = BeatLicense.objects.get(beat=beat)
        
        
        beat_license.licenses.add(_license)
        
        return beat_license


class BeatLicenseSerializer(serializers.ModelSerializer):
    
    licenses = LicenseSerializer(many=True)
    class Meta:
        model = BeatLicense
        fields = '__all__'
        