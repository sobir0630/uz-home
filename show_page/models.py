from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().all()


class ShowPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # elon matni
    image = models.ImageField(upload_to='posts/post/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # qo'shilgan sana

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=100)
    
    

