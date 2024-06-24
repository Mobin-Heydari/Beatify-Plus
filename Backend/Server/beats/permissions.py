from rest_framework import permissions

# Custom permission class to control access to objects based on ownership
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class that allows owners of an object to perform any action, 
    while non-owners can only perform safe methods (e.g., GET, HEAD, OPTIONS)
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Check if the request user has permission to access the object
        
        Args:
            request: The incoming request
            view: The view being accessed
            obj: The object being accessed
        
        Returns:
            bool: True if the user has permission, False otherwise
        """
        # If the request method is safe (e.g., GET, HEAD, OPTIONS), allow access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # If the request method is not safe, only allow access if the user is the owner of the object
        return obj.owner == request.user