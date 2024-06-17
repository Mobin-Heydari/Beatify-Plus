from django.db import models
from django.utils import timezone





class Otp(models.Model):
    
    class OtpStatus(models.TextChoices):
        EXPIRED = 'EXP', 'Expired'
        ACTIVE = 'ACT', 'Active'
        
    
    status = models.CharField(
        max_length=3,
        choices=OtpStatus.choices,
        default=OtpStatus.ACTIVE 
    )
    
    email = models.EmailField()
    
    username = models.CharField(max_length=40)
    
    user_type = models.CharField(max_length=3)
    
    password = models.CharField(max_length=16)
    
    
    token = models.CharField(
        max_length=250,
        unique=True
    )
    
    code = models.CharField(max_length=6)
    
    expiration = models.DateTimeField(
        blank=True,
        null=True,
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "One-Time Password"
        verbose_name_plural = "One-Time Passwords"
        
    
    def __str__(self):
        return f'{self.status}----{self.code}----{self.token}'
    
    
    def get_expiration(self):
        
        created = self.created
        
        expiration = created + timezone.timedelta(minutes=1)
        
        self.expiration = expiration
        
        self.save()
        
    def status_validation(self):
        
        if self.expiration <= timezone.now():
            
            self.status = 'EXP'
            
            return self.status
        else:
            return self.status