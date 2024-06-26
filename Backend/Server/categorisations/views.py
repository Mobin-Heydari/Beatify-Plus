from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from. import serializers
from.models import BeatCategorisation
from.permissions import IsOwnerOrForbidden

from moods.models import Mood
from beats.models import Beat
from tags.models import Tag



class BeatCategorisationView(APIView):
    """
    Base view for beat categorisation.
    Only authenticated users who are the owner of the beat or are staff members can make changes.
    """
    permission_classes = [IsAuthenticated, IsOwnerOrForbidden]

    def get_beat(self, slug):
        """
        Get the beat object from the slug.
        :param slug: The slug of the beat.
        :return: The beat object.
        """
        # Retrieve the beat object from the database using the provided slug
        return get_object_or_404(Beat, slug=slug)

    def get_categorisation(self, beat):
        """
        Get the categorisation for the beat.
        :param beat: The beat object.
        :return: The categorisation object.
        """
        # Retrieve the categorisation object associated with the beat
        return BeatCategorisation.objects.get(beat=beat)




class AddBeatMood(BeatCategorisationView):
    """
    View for adding a mood to a beat's categorisation.
    """
    def post(self, request, slug):
        """
        Add a mood to the beat's categorisation.
        :param request: The incoming request.
        :param slug: The slug of the beat.
        :return: A response indicating success or failure.
        """
        # Get the beat object from the slug
        beat = self.get_beat(slug)
        # Check if the user has permission to modify the beat
        self.check_object_permissions(request, beat)

        # Get the categorisation object associated with the beat
        categorisation = self.get_categorisation(beat)
        # Get the mood slug from the request
        mood_slug = request.POST.get('mood')
        # Retrieve the mood object from the database using the slug
        mood = get_object_or_404(Mood, slug=mood_slug)

        # Check if the mood is already in the categorisation
        if mood in categorisation.moods.all():
            # Return an error response if the mood is already in the categorisation
            return Response(
                {
                    'Detail': 'Mood is already in the categorisation.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Add the mood to the categorisation
            categorisation.moods.add(mood)
            # Return a success response
            return Response(
                {
                    'Detail': 'Mood added.'
                },
                status=status.HTTP_200_OK
            )


class RemoveBeatMood(BeatCategorisationView):
    """
    View for removing a mood from a beat's categorisation.
    """
    def post(self, request, slug):
        """
        Remove a mood from the beat's categorisation.
        :param request: The incoming request.
        :param slug: The slug of the beat.
        :return: A response indicating success or failure.
        """
        # Get the beat object from the slug
        beat = self.get_beat(slug)
        # Check if the user has permission to modify the beat
        self.check_object_permissions(request, beat)

        # Get the categorisation object associated with the beat
        categorisation = self.get_categorisation(beat)
        # Get the mood slug from the request
        mood_slug = request.POST.get('mood')
        # Retrieve the mood object from the database using the slug
        mood = get_object_or_404(Mood, slug=mood_slug)

        # Check if the mood is not in the categorisation
        if mood not in categorisation.moods.all():
            # Return an error response if the mood is not in the categorisation
            return Response(
                {
                    'Detail': 'Mood is not in the categorisation.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Remove the mood from the categorisation
            categorisation.moods.remove(mood)
            # Return a success response
            return Response(
                {
                    'Detail': 'Mood removed.'
                },
                status=status.HTTP_200_OK
            )


class AddBeatTag(BeatCategorisationView):
    """
    View for adding a tag to a beat's categorisation.
    """
    def post(self, request, slug):
        """
        Add a tag to the beat's categorisation.
        :param request: The incoming request.
        :param slug: The slug of the beat.
        :return: A response indicating success or failure.
        """
        #Get the beat object from the slug
        beat = self.get_beat(slug)
        # Check if the user has permission to modify the beat
        self.check_object_permissions(request, beat)

        # Get the categorisation object associated with the beat
        categorisation = self.get_categorisation(beat)
        # Get the tag slug from the request
        tag_slug = request.POST.get('tag')
        # Retrieve the tag object from the database using the slug
        tag = get_object_or_404(Tag, slug=tag_slug)

        # Check if the tag is already in the categorisation
        if tag in categorisation.tags.all():
            # Return an error response if the tag is already in the categorisation
            return Response(
                {
                    'Detail': 'Tag is already in the categorisation.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Add the tag to the categorisation
            categorisation.tags.add(tag)
            # Return a success response
            return Response(
                {
                    'Detail': 'Tag added.'
                },
                status=status.HTTP_200_OK
            )


class RemoveBeatTag(BeatCategorisationView):
    """
    View for removing a tag from a beat's categorisation.
    """
    def post(self, request, slug):
        """
        Remove a tag from the beat's categorisation.
        :param request: The incoming request.
        :param slug: The slug of the beat.
        :return: A response indicating success or failure.
        """
        # Get the beat object from the slug
        beat = self.get_beat(slug)
        # Check if the user has permission to modify the beat
        self.check_object_permissions(request, beat)

        # Get the categorisation object associated with the beat
        categorisation = self.get_categorisation(beat)
        # Get the tag slug from the request
        tag_slug = request.POST.get('tag')
        # Retrieve the tag object from the database using the slug
        tag = get_object_or_404(Tag, slug=tag_slug)

        # Check if the tag is not in the categorisation
        if tag not in categorisation.tags.all():
            # Return an error response if the tag is not in the categorisation
            return Response(
                {
                    'Detail': 'Tag is not in the categorisation.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # Remove the tag from the categorisation
            categorisation.tags.remove(tag)
            # Return a success response
            return Response(
                {
                    'Detail': 'Tag removed.'
                },
                status=status.HTTP_200_OK
            )