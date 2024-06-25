from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import BeatCategorisation
from .permissions import IsOwnerOrForbidden

from moods.models import Mood
from beats.models import Beat







class CategorisationMoodAddView(APIView):
    """
    View for adding a mood to a beat's categorisation.
    Only authenticated users who are the owner of the beat or are staff members can make changes.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrForbidden]

    def post(self, request, slug):
        """
        Add a mood to the beat's categorisation.
        :param request: The incoming request.
        :param slug: The slug of the beat.
        :return: A response indicating success or failure.
        """
        beat = get_object_or_404(Beat, slug=slug)
        self.check_object_permissions(request, beat)

        # Get the categorisation for the beat
        queryset = BeatCategorisation.objects.get(beat=beat)

        # Get the mood from the request
        mood_slug = request.POST.get('mood')
        mood = get_object_or_404(Mood, slug=mood_slug)

        # Add the mood to the categorisation
        queryset.moods.add(mood)

        # Return a response indicating success
        return Response(
            {
                'Detail':'Mood added.'
            },
            status=status.HTTP_200_OK
        )