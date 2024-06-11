from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



class User(AbstractBaseUser, PermissionsMixin):
    
    class UserTypes(models.TextChoices):
        SINGER = "SIN", "Singer"
        PRODUCER = "PRD", "Producer"
    
    
    class UserOfficialStatus(models.TextChoices):
        
        OFFICIAL = "OFL", "Official"
        UN_OFFICIAL = "UFL", "Un_Official"
    
    
    user_type = models.CharField(
        max_length=3, 
        choices=UserTypes.choices,
    )

    official_status = models.CharField(
        max_length=3,
        choices=UserOfficialStatus.choices, 
        default=UserOfficialStatus.UN_OFFICIAL,
    )
    
    email = models.EmailField(unique=True)
    
    username = models.CharField( 
        max_length=40,
        unique=True
    )
    
    joined_date = models.DateField(auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    
    class Meta:
        ordering = ['joined_date']
        verbose_name = "User"
        verbose_name_plural = "Users"


    def __str__(self):
        return self.username
    

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin