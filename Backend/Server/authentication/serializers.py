from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User



#  Token obtain serializer
class TokenObtainSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        #  User token
        token = super().get_token(user)
        
        # User custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['user_type'] = user.user_type
        token['official_status'] = user.official_status
        token['joined_date'] = str(user.joined_date)
        
        # User profiles claims
        token['f_name'] = user.user_profile.f_name
        token['l_name'] = user.user_profile.l_name
        token['bio'] = user.user_profile.bio
        
        # Returning token
        return token