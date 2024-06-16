from rest_framework import serializers

from .models import Beat, BeatInformation




class BeatSerializer(serializers.ModelSerializer):
    
    info = serializers.SerializerMethodField()
    
    # file = serializers.FileField()
    # image = serializers.FileField()
    
    class Meta:
        model = Beat
        fields = '__all__'
        
    
    def create(self, **validated_data):
        
        beat = Beat.objects.create(
            title = validated_data['title'],
            owner = self.context['request'].user,
            description = validated_data['description'],
            slug = f'{self.context['request'].user.username}-{validated_data['title']}',
            beat_file = validated_data['file'],
            image = validated_data['image']
        )
        
        beat.save()
        
        beat_info = BeatInformation.objects.create(
             beat = beat
        )
        
        beat_info.save()
        
        return beat
    
    def get_info(self, obj):
        serializer = BeatInformationSerializer(instance=obj.Beat_Info)
        return serializer.data
    
    

class BeatInformationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeatInformation
        fields = "__all__"
    