from django.db import models



class Mood(models.Model):
    
    mood = models.CharField(
        max_length=100,
        unique=True
    )
    
    slug = models.SlugField(
        max_length=100,
         unique=True
    )
    
    image = models.ImageField(
        upload_to="moods-image/"
    )

    class Meta:
        verbose_name = "Mood"
        verbose_name_plural = "Moods"

    def __str__(self):
        return self.mood