from rest_framework import serializers
from rest_framework import validators
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User



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
    
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    username = serializers.CharField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True
    )
    password_conf = serializers.CharField(
        write_only=True,
        required=True
    )
    
    user_type = serializers.CharField(
        write_only=True,
        required=True
    )
        
        
    def validate(self, attrs):
        
        if attrs['password'] == attrs['password_conf']:
            
            if len(attrs['password']) >= 8 and len(attrs['password']) <=16:
                return attrs
            else:
                raise serializers.ValidationError({"Detail":"Password length should be between 8 to 16 characters."})
        else:
            raise serializers.ValidationError({"Detail": "Passwords fields didn't match."})

        return attrs
    
    
    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        
        user.save()
        
        return user