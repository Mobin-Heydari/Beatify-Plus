from rest_framework import serializers

from .models import Beat, BeatInformation, BeatCategorisation

from categories.models import Category
from categories.serializers import CategorySerializer
from moods.serializers import MoodSerializer
from tags.serializers import TagSerializer
from users.serializers import UserSerializer





class BeatSerializer(serializers.ModelSerializer):
    # Define a serializer method field for the info field
    info = serializers.SerializerMethodField()
    
    # Define a serializer method field for the owner field
    owner = serializers.SerializerMethodField()

    # Define a serializer method field for the Categorisation field
    categorisation = serializers.SerializerMethodField()

    # Define file fields for beat_file and image
    beat_file = serializers.FileField()
    image = serializers.FileField()

    class Meta:
        # Specify the model and fields for the serializer
        model = Beat
        fields = '__all__'

    # Serialize the BeatInformation instance
    def get_info(self, obj):
        # Create a serializer instance for the BeatInformation model
        serializer = BeatInformationSerializer(instance=obj.Beat_Info)
        # Return the serialized data
        return serializer.data
    
    # Serialize the User instance
    def get_owner(self, obj):
        # Create a serializer instance for the User model
        serializer = UserSerializer(instance=obj.owner)
        # Return the serialized data
        return serializer.data

    # Serialize the BeatCategorisation instance
    def get_categorisation(self, obj):
        # Create a serializer instance for the BeatCategorisation model
        serializer = BeatCategorisationSerializer(instance=obj.Beat_Categorisation)
        # Return the serialized data
        return serializer.data

    # Create a new Beat instance
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

        # Get the category name from the validated data
        category_name = validated_data['category']
        # Get the Category instance from the database
        category = Category.objects.get(category=category_name)
        # Create a new BeatCategorisation instance
        beat_categorisation = BeatCategorisation.objects.create(
            beat=beat,
            category=category
        )
        # Save the BeatCategorisation instance
        beat_categorisation.save()

        # Return the created Beat instance
        return beat

    # Update an existing Beat instance
    def update(self, instance, validated_data):
        # Update the title and description fields
        if 'title' in validated_data:
            instance.title = validated_data['title']
        if 'description' in validated_data:
            instance.description = validated_data['description']
        if 'title' in validated_data:
            instance.slug = f'{instance.owner.username}-{validated_data["title"]}'

        # Save the changes
        instance.save()

        # Handle file updates
        if 'beat_file' in validated_data:
            # Update the beat_file field
            instance.beat_file = validated_data['beat_file']

        # Handle file updates
        if 'image' in validated_data:
            # Update the image field
            instance.image = validated_data['image']

        # Save the changes
        instance.save()

        # Return the updated Beat instance
        return instance


class BeatInformationSerializer(serializers.ModelSerializer):
    # Specify the model and fields for the serializer
    class Meta:
        model = BeatInformation
        fields = "__all__"


class BeatCategorisationSerializer(serializers.ModelSerializer):
    # Serialize the category field
    category = serializers.SerializerMethodField()
    
    # Serialize the moods field
    moods = MoodSerializer(
        read_only=True,
        many=True
    )
    
    # Serialize the tags field
    tags = TagSerializer(
        read_only=True,
        many=True
    )
    
    # Serialize the Category instance
    def get_category(self, obj):
        serializer = CategorySerializer(instance=obj.category)
        return serializer.data
    
    class Meta:
        model = BeatCategorisation
        fields = "__all__"