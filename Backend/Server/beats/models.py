from django.db import models

from categories.models import Category
from users.models import User
from moods.models import Mood
from tags.models import Tag

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
        default='Draft',
        verbose_name='published status',
    )  # Field to store the published status of the Beat

    # Represents the status of the Beat
    status = models.CharField(
        max_length=8, 
        choices=Status.choices, 
        default='Checking'
    )  # Field to store the status of the Beat

    # Foreign key to the User who owns the Beat
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Beat_Owner',
        blank=True,
        null=True
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
        unique=True,
        blank=True,
        null=True
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
        blank=True,
        null=True,
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
    

class BeatCategorisation(models.Model):
    # One-to-one field to the Beat model, establishing a direct relationship between a Beat and its categorization
    beat = models.OneToOneField(
        Beat,
        on_delete=models.CASCADE,
        related_name='Beat_Categorisation'
    )  # Link to the Beat model, allowing for easy access to the related Beat instance
    
    # Foreign key to the Category model, specifying the genre and type of the beat
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='Beat_Categorisation_Category'
    )  # Link to the Category model, enabling categorization of beats
    
    # Many-to-many field for Moods, allowing a beat to have multiple moods and a mood to be associated with multiple beats
    moods = models.ManyToManyField(
        Mood, 
        blank=True
    )  # Optional field, allowing for moods to be specified or not
    
    # Many-to-many field for Tags, enabling a beat to have multiple tags and a tag to be associated with multiple beats
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )  # Optional field, allowing for tags to be specified or not
    
    class Meta:
        # Specify the ordering of BeatCategorisation instances based on the related Beat's title
        ordering = ['beat']
        # Set the verbose name for a single instance of BeatCategorisation
        verbose_name = 'Beat Categorisation'
        # Set the verbose name for multiple instances of BeatCategorisation
        verbose_name_plural = 'Beat Categorisations'
    
    
    def __str__(self):
        # Return a string representation of the BeatCategorisation instance, combining the beat title and category
        return f'{self.beat.title}---{self.category.category}'