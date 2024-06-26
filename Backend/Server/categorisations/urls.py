from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "beats"


urlpatterns = [
    
    # Beat tags add and remove url
    path('beat/add-mood/<slug:slug>/', views.AddBeatMood.as_view(), name="beats_add_mood"),
    path('beat/remove-mood/<slug:slug>/', views.RemoveBeatMood.as_view(), name="beats_remove_mood"),
    
    # Beat tags add and remove url
    path('beat/add-tag/<slug:slug>/', views.AddBeatTag.as_view(), name="beats_add_tag"),
    path('beat/remove-tag/<slug:slug>/', views.RemoveBeatTag.as_view(), name="beats_remove_tag"),
]

