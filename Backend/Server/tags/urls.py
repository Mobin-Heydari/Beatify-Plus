from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "tags"


urlpatterns = [
    
]


# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.TagViewSet, basename='tags')
# Complaining the routers
urlpatterns += router.urls
