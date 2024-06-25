from rest_framework import serializers

from .models import BeatCategorisation

from categories.serializers import CategorySerializer
from moods.serializers import MoodSerializer
from tags.serializers import TagSerializer






class BeatCategorisationSerializer(serializers.ModelSerializer):
    # Serialize the category field
    category = serializers.SerializerMethodField()
    
    # Serialize the moods field
    moods = MoodSerializer(
        many=True
    )
    
    # Serialize the tags field
    tags = TagSerializer(
        many=True
    )
    
    class Meta:
        model = BeatCategorisation
        fields = "__all__"
        
        
    # Serialize the Category instance
    def get_category(self, obj):
        serializer = CategorySerializer(instance=obj.category)
        return serializer.data
