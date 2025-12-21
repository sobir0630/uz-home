from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Annoncements(models.Model):
    HOME_CATEGORY_CHOICES = (
        ('apartment', 'Kvartira'),
        ('house', 'Hovli uy'),
        ('new_building', 'Yangi qurilgan uy'),
        ('commercial', 'Tijorat bino'),
        ('land', 'Yer uchastkasi'),
        ('rent_apartment', 'Ijara kvartira'),
        ('rent_house', 'Ijara hovli uy'),
    )
    
    STATUS_CHOISES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/post/', null=True, blank=True)
    seller_contact = models.CharField(max_length=100, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=150, choices=HOME_CATEGORY_CHOICES, default='house', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOISES, default='published', null=True, blank=True)
       
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            
            self.slug = slugify(self.name)
                
        super().save(*args, **kwargs)
    
    
    object = models.Manager()  # The default manager
    published = PublishedManager()  # Custom manager for published announcements

        
