from django.urls import path

from . import views



app_name = "license"


urlpatterns = [
    path('beat/<slug:slug>/', views.BeatLicenses.as_view(), name="beat_licenses"),
]
