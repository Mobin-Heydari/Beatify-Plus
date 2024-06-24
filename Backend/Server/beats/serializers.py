from rest_framework import serializers

from.models import Beat, BeatInformation, BeatCategorisation

from categories.models import Category
from categories.serializers import CategorySerializer



class BeatSerializer(serializers.ModelSerializer):
    # Define a serializer method field for the info field
    info = serializers.SerializerMethodField()

    # Define a serializer method field for the Categorisation field
    categorisation = serializers.SerializerMethodField()

    # Define file fields for beat_file and image
    beat_file = serializers.FileField()
    image = serializers.FileField()

    class Meta:
        # Specify the model and fields for the serializer
        model = Beat
        fields = '__all__'

    def get_info(self, obj):
        # Return the serialized BeatInformation instance
        serializer = BeatInformationSerializer(instance=obj.Beat_Info)
        return serializer.data

    def get_categorisation(self, obj):
        # Return the serialized BeatCategorisation instance
        serializer = BeatCategorisationSerializer(instance=obj.Beat_Categorisation)
        return serializer.data

    def create(self, validated_data):
        # Get the request object from the context
        request = self.context.get('request')

        # Create a new Beat instance
        beat = Beat.objects.create(
            title=validated_data['title'],
            owner=request.user,
            slug=f'{request.user.username}-{validated_data["title"]}',
            beat_file=validated_data['beat_file'],
            image=validated_data['image']
        )

        # Save the Beat instance
        beat.save()

        # Create a new BeatInformation instance
        beat_info = BeatInformation.objects.create(
            beat=beat
        )
        # Save the BeatInformation instance
        beat_info.save()

        category_name = validated_data['category']
        category = Category.objects.get(category=category_name)
        # Create a new BeatCategorisation instance
        beat_categorisation = BeatCategorisation.objects.create(
            beat=beat,
            category=category
        )
        # save the BeatCategorisation instance
        beat_categorisation.save()

        return beat

    def update(self, instance, validated_data):
        # Update the title and description fields
        if 'title' in validated_data:
            instance.title = validated_data['title']
        if 'description' in validated_data:
            instance.description = validated_data['description']
        if 'title' in validated_data:
            instance.slug = f'{instance.owner.username}-{validated_data["title"]}'

        instance.save()

        # Handle file updates
        if 'beat_file' in validated_data:
            # Update the beat_file field
            instance.beat_file = validated_data['beat_file']

        # Handle file updates
        if 'image' in validated_data:
            # Update the image field
            instance.image = validated_data['image']

        instance.save()

        return instance
    

class BeatInformationSerializer(serializers.ModelSerializer):
    # Specify the model and fields for the serializer
    class Meta:
        model = BeatInformation
        fields = "__all__"


class BeatCategorisationSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        serializer = CategorySerializer(instance=obj.category)
        return serializer.data

    class Meta:
        model = BeatCategorisation
        fields = "__all__"

    class Meta:
        model = BeatCategorisation
        fields = "__all__"