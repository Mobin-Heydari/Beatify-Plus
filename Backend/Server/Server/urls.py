from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('auth/', include('authentication.urls', namespace="authentication")),
    path('beats/', include('beats.urls', namespace="beats")),
    path('users/', include('users.urls', namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
