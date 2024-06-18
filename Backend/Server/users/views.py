from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from . import serializers
from .models import User



class UserViewSet(ViewSet):
    """
    A ViewSet for handling user-related API requests.
    """
    
    def list(self, request):
        """
        Return a list of all users.
        """
        queryset = User.objects.all()
        serializer = serializers.UserSerializer(instance=queryset, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, pk):
        """
        Return a single user by username.
        """
        query = get_object_or_404(User, username=pk)
        serializer = serializers.UserSerializer(instance=query)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
    def update(self, request, pk):
        """
        Update user data.
        
        Only allows the requesting user to update their own data.
        """
        user = get_object_or_404(User, username=pk)
        
        # Check if the requesting user is authenticated
        if request.user.is_authenticated:
            # Check if the requesting user is the same as the user being updated
            if user == request.user:
                # Update the user instance using the UserSerializer
                serializer = serializers.UserSerializer(instance=user, data=request.data, partial=True)
                
                # If the data is valid, update the instance and return a 200 OK response
                if serializer.is_valid(raise_exception=True):
                    serializer.update(instance=user, validated_data=serializer.validated_data)
                    return Response(
                        serializer.data,
                        status=status.HTTP_200_OK
                    )
                else:
                    # Return a 400 Bad Request response if the data is invalid
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                # Return a 403 Forbidden response if the requesting user is not the same as the user being updated
                return Response(
                    {
                        'Detail':'You dont have the permission.'
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
        else:
            # Return a 401 Unauthorized response if the user is not authenticated
            return Response(
                {
                    'Detail':'you are not authenticated.'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )