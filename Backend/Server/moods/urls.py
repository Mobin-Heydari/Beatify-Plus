from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "moods"


urlpatterns = [
    
]


# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.MoodViewSet, basename='moods')
# Complaining the routers
urlpatterns += router.urls
