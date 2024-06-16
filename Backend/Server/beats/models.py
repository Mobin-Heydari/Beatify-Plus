from django.db import models
from users.models import User
from . import managers



class Beat(models.Model):
    # Define the published status choices (Draft, Private, Published)
    class PublishedStatus(models.Choices):
        DRAFT = 'Draft'
        PRIVATE = 'Private'
        PUBLISHED = 'Published'

    # Define the status choices (Accepted, Checking, Rejected)
    class Status(models.Choices):
        ACCEPTED = 'Accepted'
        CHECKING = 'Checking'
        REJECTED = 'Rejected'

    # Represents the published_status of the Beat
    published_status = models.CharField(
        max_length=9,
        choices=PublishedStatus.choices,
        default=PublishedStatus.DRAFT,
        verbose_name='published status',
    )  # Field to store the published status of the Beat

    # Represents the status of the Beat
    status = models.CharField(
        max_length=8, 
        choices=Status.choices, 
        default=Status.CHECKING
    )  # Field to store the status of the Beat

    # Foreign key to the User who owns the Beat
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Beat_Owner'
    )  # Foreign key to the User model

    # Title of the Beat
    title = models.CharField(
        max_length=50,
        blank=False,
        unique=True,
        null=False
    )  # Field to store the title of the Beat

    # Unique slug for the Beat
    slug = models.SlugField(
        max_length=255,
        unique=True
    )  # Field to store the slug of the Beat

    # Image associated with the Beat
    image = models.ImageField(
        upload_to='beats/images',
        blank=True
    )  # Field to store the image associated with the Beat

    # File associated with the Beat
    beat_file = models.FileField(
        verbose_name='beat file',
        upload_to='beats/files',
        blank=True
    )  # Field to store the file associated with the Beat

    # Description of the Beat
    description = models.TextField(
        blank=True,
        null=True
    )  # Field to store the description of the Beat

    # Timestamp when the Beat was created
    created = models.DateTimeField(auto_now_add=True)

    # Timestamp when the Beat was last updated
    updated = models.DateTimeField(auto_now=True)

    # Default manager for the Beat model
    objects = models.Manager()

    # Manager for accepted Beats
    accepted = managers.AcceptedManager()

    # Manager for rejected Beats
    rejected = managers.RejectedManager()

    # Manager for Beats under checking
    checking = managers.CheckingManager()

    # Manager for published Beats
    published = managers.PublishedManager()

    # Manager for draft Beats
    drafts = managers.DraftManager()

    # Manager for private Beats
    private = managers.PrivateManager()
    
    # Managers for the Beat model
    objects = models.Manager()
    accepted_manager = managers.AcceptedManager()
    rejected_manager = managers.RejectedManager()
    checking_manager = managers.CheckingManager()
    published_manager = managers.PublicManager()
    drafts_manager = managers.DraftManager()
    private_manager = managers.PrivateManager()
    class Meta:
        # Meta options for the Beat model
        ordering = ['-created']
        verbose_name = "Beat"
        verbose_name_plural = "Beats"

    def __str__(self):
        # Returns a string representation of the Beat
        return f'{self.title}--{self.owner.username}'
    


class BeatInformation(models.Model):
    # One-to-one field to the Beat model
    beat = models.OneToOneField(
        Beat,
        on_delete=models.CASCADE,
        related_name='Beat_Info'
    )  # Link to the Beat model

    # Beats per minute (BPM) of the Beat
    bpm = models.BigIntegerField(
        blank=True,
        null=True
    )  # Field to store the BPM of the Beat

    # Keys of the Beat
    keys = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )  # Field to store the keys of the Beat

    # Publish date of the Beat
    publish = models.DateField(
        blank=True,
        null=True
    )  # Field to store the publish date of the Beat

    # Number of plays of the Beat
    plays = models.IntegerField(default=0) # Field to store the number of plays of the Beat, defaulting to 0

    class Meta:
        # Meta options for the BeatInformation model
        ordering = ['-beat']
        verbose_name = "Beat Information"
        verbose_name_plural = "Beats Information"

    def __str__(self):
        # Returns a string representation of the BeatInformation
        return f'{self.publish}-{self.beat.title}'