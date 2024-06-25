from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "beats"


urlpatterns = [
    path('beat/add-mood/<slug:slug>/', views.CategorisationMoodAddView.as_view(), name="beats_add_mood"),
]

