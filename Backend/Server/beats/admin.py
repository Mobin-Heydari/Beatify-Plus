from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Beat)
admin.site.register(models.BeatInformation)
admin.site.register(models.BeatCategorisation)