from django.db import models
from users.models import User



class Beat(models.Model):
    
    class PublishedStatus(models.Choices):
        
        DRAFT = 'Draft'
        PRIVATE = 'Private'
        PUBLISHED = 'Published'
    
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
    )

    # Represents the status of the Beat
    status = models.CharField(
        max_length=8, 
        choices=Status.choices, 
        default=Status.CHECKING
    )
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Beat_Owner'
    )
    
    title = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )
    
    slug = models.SlugField(
        max_length=255,
        unique=True
    )
    
    image = models.ImageField(
        upload_to='beats/images',
        blank=True
    )
    
    beat_file = models.FileField(
        verbose_name='beat file',
        upload_to='beats/files',
        blank=True
    )
    
    description = models.TextField(
        blank=True,
        null=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        verbose_name = "Beat"
        verbose_name_plural = "Beats"
    
    def __str__(self):
        
        return f'{self.title}--{self.owner.username}'
    


class BeatInformation(models.Model):
    
    beat = models.OneToOneField(
        Beat,
        on_delete=models.CASCADE,
        related_name='Beat_Info'
    )
    
    bpm = models.BigIntegerField(
        blank=True,
        null=True
    )
    
    keys = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    
    publish = models.DateField(
        blank=True,
        null=True
    )
    
    plays = models.IntegerField(default=0)
    
    
    class Meta:
        ordering = ['-beat']
        verbose_name = "Beat Information"
        verbose_name_plural = "Beats Information"
        
    
    def __str__(self):
        return f'{self.publish}-{self.beat.title}'