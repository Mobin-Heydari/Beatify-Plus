from django.contrib.auth.password_validation import validate_password
from django.utils.crypto import get_random_string

from rest_framework import serializers
from rest_framework import validators

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

from .models import Otp

from random import randint


class TokenObtainSerializer(TokenObtainPairSerializer):
    # Custom Token Obtain Serializer that inherits from TokenObtainPairSerializer
    
    @classmethod
    def get_token(cls, user):
        # Override the get_token method to add custom claims to the token
        
        # Call the parent class's get_token method to get the default token
        token = super().get_token(user)
        
        # Add custom claims to the token
        # User custom claims
        token['username'] = user.username  # Add the user's username to the token
        token['email'] = user.email  # Add the user's email to the token
        token['user_type'] = user.user_type  # Add the user's type to the token
        token['official_status'] = user.official_status  # Add the user's official status to the token
        token['joined_date'] = str(user.joined_date)  # Add the user's joined date to the token
        
        # User profiles claims
        token['f_name'] = user.user_profile.f_name  # Add the user's first name to the token
        token['l_name'] = user.user_profile.l_name  # Add the user's last name to the token
        token['bio'] = user.user_profile.bio  # Add the user's bio to the token
        
        # Return the token with the added custom claims
        return token



class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
        write_only=True,
        required=True
    )
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True
    )



    
class UserRegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration
    """
    
    # Email field with unique validator to ensure email is not already in use
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    # Username field with unique validator to ensure username is not already in use
    username = serializers.CharField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    # Password field with custom validator and write-only access
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True
    )

    # Password confirmation field with write-only access
    password_conf = serializers.CharField(
        write_only=True,
        required=True
    )

    # User type field with write-only access
    user_type = serializers.CharField(
        write_only=True,
        required=True
    )
    
    
    def validate(self, attrs):
        """
        Validate the serializer data
        """
        # Check if the password and password confirmation match
        if attrs['password'] == attrs['password_conf']:
            # Check if the password length is between 8 and 16 characters
            if len(attrs['password']) >= 8 and len(attrs['password']) <= 16:
                return attrs
            else:
                raise serializers.ValidationError({"Detail": "Password length should be between 8 to 16 characters."})
        else:
            raise serializers.ValidationError({"Detail": "Passwords fields didn't match."})
    
    def create(self, validated_data):

        # Create a new OTP object and save it to the database

        # Generate a random code and token
        code = randint(100000, 999999)
        token = get_random_string(250)
        
        # Create a new OTP object with the validated data
        otp = Otp.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            password=validated_data['password'],
            token=token,
            code=code
        )
        
        # Save the OTP object to the database
        otp.save()
        
        return otp
    
class OtpSerializer(serializers.Serializer):
    
    code = serializers.CharField(write_only=True, required=True)