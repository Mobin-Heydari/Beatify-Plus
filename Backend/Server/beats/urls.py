from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views



app_name = "beats"


urlpatterns = [
    path('categoriations/add-mood/<slug:slug>/', views.CategorisationMoodAddView.as_view(), name="categoriations_add_mood")
]


# Routers
router = DefaultRouter()
# ProfileViewSet router
router.register(r'', views.BeatViewSet, basename='beats')
# Complaining the routers
urlpatterns += router.urls
