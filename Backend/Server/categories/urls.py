from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "categories"


urlpatterns = [
    
]


# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.CategoryViewSet, basename='categories')
# Complaining the routers
urlpatterns += router.urls
