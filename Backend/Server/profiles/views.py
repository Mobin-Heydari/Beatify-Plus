from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
from .paginations import ProfilePagination
from users.models import User




class ProfileViewSet(ViewSet, ProfilePagination):
    
    # List method for profiles
    def list(self, request):
        # Getting profiles queries 
        queryset = UserProfile.objects.all()
        # Paginating querysets
        result = self.paginate_queryset(queryset, request)
        # Serializing the queries
        serializer = UserProfileSerializer(instance=result, many=True)
        # Returning the paginated serializered data
        return self.get_paginated_response(serializer.data)
    
    # Retrieve method for profiles
    def retrieve(self, request, pk):
        # Getting profile queryset by pk
        queryset = get_object_or_404(UserProfile, id=pk)
        # Serializing the user profile queryset
        serializer = UserProfileSerializer(instance=queryset)
        # Returning the serialized data with http 200 status code
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # Update method for profiles
    def update(self, request):
        # Make sure the requested user is authenticated for having better secuirety performance
        if request.user.is_authenticated == True:
            # Getting requested user 
            user = request.user
            # Getting user profile queryset 
            # If user dosn't have any profile this get_object_or_404 will show the 404 not found error to user 
            queryset = get_object_or_404(UserProfile, user=user)
            # Serializing the user profile queryset and sending the data request for updating
            serializer = UserProfileSerializer(instance=queryset, data=request.data, partial=True)
            # Validating requested data
            if serializer.is_valid(raise_exception=True):
                # Saving the data updated
                serializer.save()
                # Returning serialized data with http 200 status code
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # Returning the serializer errors with http 400 bad request status code
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Returning the authentication errors with http 401 unauthorized status code
            return Response({'Error':'You need to authenticate your self'}, status=status.HTTP_401_UNAUTHORIZED)