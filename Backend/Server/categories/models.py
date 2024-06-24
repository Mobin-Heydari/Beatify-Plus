from django.db import models



class Category(models.Model):
    
    category = models.CharField(
        max_length=100,
        unique=True
    )
    
    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    
    image = models.ImageField(
        upload_to="categories-images/"
    )


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.name
