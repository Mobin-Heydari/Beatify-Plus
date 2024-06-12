from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('auth/', include('authentication.urls', namespace="authentication")),
]
