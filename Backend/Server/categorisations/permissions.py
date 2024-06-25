from rest_framework import permissions




class IsOwnerOrForbidden(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        return obj.owner == request.user