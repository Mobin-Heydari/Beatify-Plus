from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView, Response
from rest_framework import status 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from users.models import User


class TokenObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainSerializer
    

class UserLogin(APIView):
    """
    API View for user login
    """
    def post(self, request):
        """
        Handle POST request for user login
        """
        # Check if the user is not already authenticated
        if request.user.is_authenticated == False:
            # Create a serializer instance with the request data
            serializer = serializers.UserLoginSerializer(data=request.data)
            
            # Validate the serializer data
            if serializer.is_valid(raise_exception=True):
                # Authenticate the user using the email and password
                user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
                
                # Check if the user is authenticated
                if user is not None:
                    # Check if the user account is active
                    if user.is_active:
                        # Generate a refresh token for the user
                        token = RefreshToken.for_user(user)
                        # Return the refresh and access tokens in the response
                        return Response({'refresh': str(token), 'access': str(token.access_token)}, status=status.HTTP_200_OK)
                    else:
                        # Return an error response if the user account is disabled
                        return Response({'Detail':'User account is disabled'}, status=status.HTTP_403_FORBIDDEN)
                else:
                    # Return an error response if the username or password is invalid
                    return Response({'Detail':'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Return an error response if the serializer validation fails
                return Response({'Detail':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response if the user is already logged in
            return Response({'Detail':'You are already logged in'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserRegister(APIView):
    """
    API View for user registration
    """
    def post(self, request):
        """
        Handle POST request for user registration
        """
        # Check if the user is not already authenticated
        if request.user.is_authenticated == False:
            # Create a serializer instance with the request data
            serializer = serializers.UserRegisterSerializer(data=request.data)
            # Validate the serializer data
            if serializer.is_valid(raise_exception=True):
                #  Saving the validated data 
                serializer.save()
                #  caching the user by validated data email key
                user_email = serializer.validated_data['email']
                # 
                user = User.objects.get(email = user_email)
                
                # Generate a refresh token for the user
                token = RefreshToken.for_user(user)
                
                # Return a successful response with the token
                return Response(
                    {
                        'Detail': {
                            'Massage' : 'User created successfully',  # Return a success message
                            'Token' : {
                                'refresh' : str(token),  # Return the refresh token
                                'access' : str(token.access_token)  # Return the access token
                            }
                        }
                    }, status=status.HTTP_201_CREATED
                )
            else:
                # Return an error response if the serializer validation fails
                return Response({'Detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response if the user is already logged in
            return Response({'Detail':'You are already logged in'}, status=status.HTTP_400_BAD_REQUEST)