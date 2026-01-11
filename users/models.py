from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True
    )
    password = models.CharField(
        max_length=128, null=True, 
        blank=True
    )
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="Foydalanuvchining telefon raqami"
    )
    telegram = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        help_text="Foydalanuvchining Telegram username (faqat username, @ belgisiz)"
    )
    
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

        
    def __str__(self):
        return self.username
