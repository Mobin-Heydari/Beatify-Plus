from django.db import models



class Tag(models.Model):

    tag = models.CharField(
        max_length=100,
         unique=True
    )

    slug = models.SlugField(
        max_length=100,
         unique=True
    )
    
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        
    def __str__(self):
        return self.name