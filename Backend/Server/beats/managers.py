from django.db.models import Manager
from . import models


class AcceptedManager(Manager):
    def get_queryset(self):
        """Filter records based on the 'accepted' status."""
        return super().get_queryset().filter(status=models.Beat.Status.ACCEPTED)

class RejectedManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=models.Beat.Status.REJECTED)

class CheckingManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=models.Beat.Status.CHECKIND)

class DraftManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_status=models.Beat.MainStatus.DRAFT)
    
class PublicManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_status=models.Beat.MainStatus.PUBLIC)

class PrivateManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(main_status=models.Beat.MainStatus.PRIVATE)