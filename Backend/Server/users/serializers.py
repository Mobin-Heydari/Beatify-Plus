from rest_framework import serializers

from .models import User




class UserSerializer(serializers.ModelSerializer):
    # Define the fields to be serialized
    class Meta:
        model = User
        fields = '__all__'
        
    # Custom update method
    def update(self, instance, validated_data):
        # Update username if provided
        if 'username' in validated_data:
            instance.username = validated_data['username']
        
        # Update email if provided
        if 'email' in validated_data:
            instance.email = validated_data['email']
        
        # Update user_type if provided
        if 'user_type' in validated_data:
            instance.user_type = validated_data['user_type']
        
        # Save the updated instance
        instance.save()
        
        return instance