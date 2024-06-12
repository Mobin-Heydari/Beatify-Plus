from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


app_name = "profiles"


urlpatterns = [
    
]

# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.ProfileViewSet, basename='profile')
# Complaining the routers
urlpatterns += router.urls
