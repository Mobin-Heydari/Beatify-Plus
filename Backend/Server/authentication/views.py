from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from rest_framework.views import APIView, Response
from rest_framework import status 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

from . import serializers
from .models import Otp


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
        if request.user.is_authenticated == False:  # Simplified the condition
            # Create a serializer instance with the request data
            serializer = serializers.UserLoginSerializer(data=request.data)
            
            # Validate the serializer data
            if serializer.is_valid(raise_exception=True):
                # Authenticate the user using the email and password
                user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
                
                # Check if the user is authenticated
                if user:
                    # Check if the user account is active
                    if user.is_active:
                        # Generate a refresh token for the user
                        token = RefreshToken.for_user(user)
                        # Return the refresh and access tokens in the response
                        return Response(
                            {'refresh': str(token), 'access': str(token.access_token)},
                            status=status.HTTP_200_OK
                        )
                    else:
                        # Return an error response if the user account is disabled
                        return Response(
                            {'Detail': 'User account is disabled'},
                            status=status.HTTP_403_FORBIDDEN
                        )
                else:
                    # Return an error response if the username or password is invalid
                    return Response(
                        {'Detail': 'Invalid email or password'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                # Return an error response if the serializer validation fails
                return Response(
                    {'Detail': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # Return an error response if the user is already logged in
            return Response(
                {'Detail': 'You are already logged in'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
class UserRegister(APIView):
    """
    API View for user registration
    """
    def post(self, request):
        """
        Handle POST request for user registration
        """
        # Check if the user is not already authenticated
        if request.user.is_authenticated == False:  # Simplified the condition
            # Create a serializer instance with the request data
            serializer = serializers.UserRegisterSerializer(data=request.data)
            
            # Validate the serializer data
            if serializer.is_valid(raise_exception=True):
                # Save the validated data
                serializer.save()
                
                # Get the email from the validated data
                email = serializer.validated_data['email']
                
                # Get the OTP object associated with the email
                otp = Otp.objects.get(email=email)
                
                send_mail(
                    subject = 'Beatify Plus one-time password',
                    message = f'please enter this code to continue. (code:{otp.code})',
                    from_email = 'email@hip-hop-tweety.com',
                    recipient_list = [str(email)],
                    fail_silently = False
                )
                
                # Return a successful response with the token
                return Response(
                    {
                        'Detail': {
                            'Message': 'Otp created successfully',  # Fixed typo in "Massage"
                            'token': otp.token
                        }
                    }, status=status.HTTP_201_CREATED
                )
            else:
                # Return an error response if the serializer validation fails
                return Response({'Detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Return an error response if the user is already logged in
            return Response({'Detail': 'You are already logged in'}, status=status.HTTP_400_BAD_REQUEST)
        


class CheckOtp(APIView):
    """
    API View to handle OTP verification and user creation
    """
    def post(self, request, token):
        """
        Handle POST request to verify OTP and create user
        """
        # Check if the user is not authenticated
        if request.user.is_authenticated == False:
            # Get the OTP object from the database using the provided token
            otp = get_object_or_404(Otp, token=token)
            if otp:
                # Serialize the request data using the OtpSerializer
                serializer = serializers.OtpSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    # Extract the code from the validated data
                    code = serializer.validated_data['code']
                    # Check if the OTP code matches the provided code
                    if otp.code == code:
                        # Mark the OTP as used
                        otp.is_used = True
                        otp.save()
                        # Create a new user using the OTP details
                        user = User.objects.create_user(
                            email=otp.email,
                            username=otp.username,
                            password=otp.password,
                            user_type=otp.user_type
                        )
                        user.save()
                        # Authenticate the user
                        authenticate(user)
                        # Generate a refresh token for the user
                        token = RefreshToken.for_user(user)
                        # Return a success response with the tokens
                        return Response(
                            {
                                'Detail': {
                                    'Message': 'User created successfully',  # Return a success message
                                    'Token': {
                                        'refresh': str(token),  # Return the refresh token
                                        'access': str(token.access_token)  # Return the access token
                                    }
                                }
                            }, status=status.HTTP_201_CREATED
                        )
                    else:
                        # Return an error response if the OTP code is invalid
                        return Response(
                            {'Detail': 'otp code is invalid'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    # Return an error response if the serializer is invalid
                    return Response(
                        {'Detail': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                # Return an error response if the OTP does not exist
                return Response(
                    {'Detail': 'otp is not exists'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            # Return an error response if the user is already authenticated
            return Response(
                {'Detail': 'you are authenticated'},
                status=status.HTTP_400_BAD_REQUEST
            )