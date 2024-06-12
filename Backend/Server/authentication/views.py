from rest_framework.views import APIView, Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from . import serializers
from users.models import User


class TokenObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainSerializer