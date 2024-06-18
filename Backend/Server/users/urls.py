from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "users"


urlpatterns = [
    
]


# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.UserViewSet, basename='users')
# Complaining the routers
urlpatterns += router.urls
