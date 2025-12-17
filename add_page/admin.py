from django.contrib import admin
from .models import annoncements

# Register your models here.
@admin.register(annoncements)
class annoncementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'published', 'description', 'image', 'seller_contact', 'created_at', 'updated_at')
    list_filter = ('user', 'published', 'created_at')
    search_fields = ('name', 'price', 'location', 'description', 'seller_contact')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'created_at'
    ordering = ('published', 'created_at')