from django.db import models

from beats.models import Beat



# License model, represents a license that can be purchased for a beat
class License(models.Model):
    
    # Title of the license (e.g. "Basic", "Premium", etc.)
    title = models.CharField(max_length=200)
    
    # Description of the license
    description = models.TextField()
    
    # Price of the license
    price = models.BigIntegerField()

    class Meta:
        verbose_name = 'License'
        verbose_name_plural = 'Licenses'

    def __str__(self):
        return self.title  # corrected, assuming you want to return the title


# LicenseFiles model, represents a file associated with a license
class LicenseFile(models.Model):
    
    # Foreign key to the License model, represents the license that this file belongs to
    license_model = models.ForeignKey(
        License,
        on_delete=models.CASCADE,
        related_name='license_files'
    )
    
    # Name of the file
    file_name = models.CharField(max_length=100)
    
    # The file itself
    file = models.FileField(
        verbose_name='license file',
        upload_to='license/files/'  # consider using a dynamic upload path
    )

    class Meta:
        verbose_name = 'License File'
        verbose_name_plural = 'License Files'

    def __str__(self):
        return self.file_name


# BeatLicenses model, represents the licenses associated with a beat
class BeatLicense(models.Model):
    
    # Foreign key to the Beat model, represents the beat that these licenses belong to
    beat = models.ForeignKey(
        'beats.Beat',  # assuming the Beat model is in the beats app
        on_delete=models.CASCADE,
        related_name='beat_licenses'
    )
    
    # Many-to-many field to store licenses associated with this beat
    licenses = models.ManyToManyField(
        License,
        blank=True
    )

    class Meta:
        verbose_name = 'Beat License'
        verbose_name_plural = 'Beats Licenses'

    def __str__(self):
        return f'{self.beat.title}'  # returns the title of the associated beat