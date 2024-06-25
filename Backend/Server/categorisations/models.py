from django.db import models

from beats.models import Beat
from categories.models import Category
from moods.models import Mood
from tags.models import Tag



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