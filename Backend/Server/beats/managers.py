from django.db.models import Manager
from . import models


class AcceptedManager(Manager):
    # Custom manager to filter Beats with 'accepted' status
    def get_queryset(self):
        """Filter records based on the 'accepted' status."""
        return super().get_queryset().filter(status=models.Beat.Status.ACCEPTED)
    # Returns a queryset of Beats with 'accepted' status

class RejectedManager(Manager):
    # Custom manager to filter Beats with 'rejected' status
    def get_queryset(self):
        """Filter records based on the 'rejected' status."""
        return super().get_queryset().filter(status=models.Beat.Status.REJECTED)
    # Returns a queryset of Beats with 'rejected' status

class CheckingManager(Manager):
    # Custom manager to filter Beats with 'checking' status
    def get_queryset(self):
        """Filter records based on the 'checking' status."""
        return super().get_queryset().filter(status=models.Beat.Status.CHECKING)
    # Returns a queryset of Beats with 'checking' status

class DraftManager(Manager):
    # Custom manager to filter Beats with 'draft' published status
    def get_queryset(self):
        """Filter records based on the 'draft' published status."""
        return super().get_queryset().filter(main_status=models.Beat.PublishedStatus.DRAFT)
    # Returns a queryset of Beats with 'draft' published status

class PublishedManager(Manager):
    # Custom manager to filter Beats with 'published' published status
    def get_queryset(self):
        """Filter records based on the 'published' published status."""
        return super().get_queryset().filter(main_status=models.Beat.PublishedStatus.PUBLISHED)
    # Returns a queryset of Beats with 'published' published status

class PrivateManager(Manager):
    # Custom manager to filter Beats with 'private' published status
    def get_queryset(self):
        """Filter records based on the 'private' published status."""
        return super().get_queryset().filter(main_status=models.Beat.PublishedStatus.PRIVATE)
    # Returns a queryset of Beats with 'private' published status