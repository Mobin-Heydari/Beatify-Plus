from django.contrib import admin

from . import models


admin.site.register(models.BeatLicense)
admin.site.register(models.License)
admin.site.register(models.LicenseFile)