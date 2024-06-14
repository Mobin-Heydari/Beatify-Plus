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
    
    email = models.EmailField(unique=True)
    
    username = models.CharField( 
        max_length=40,
        unique=True
    )
    
    user_type = models.CharField(max_length=3)
    
    password = models.CharField(max_length=16)
    
    
    token = models.CharField(
        max_length=250,
        unique=True
    )
    
    code = models.CharField(max_length=6)
    
    expiration = models.DateTimeField(
        default=timezone.now() + timezone.timedelta(minutes=1)
    )
    
    class Meta:
        verbose_name = "One-Time Password"
        verbose_name_plural = "One-Time Passwords"
        
    
    def __str__(self):
        return f'{self.status}----{self.code}----{self.token}'
        
        
    def status_validation(self):
        
        if self.expiration >= timezone.now():
            
            self.status = self.OtpStatus.EXPIRED
            
            if self.status == self.OtpStatus.EXPIRED:
        
                self.delete()
                
                return 'Deleted'
            else:
                return 'Is not expired'
        else:
            return 'Is not expired'