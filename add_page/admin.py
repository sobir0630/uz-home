from django.contrib import admin
from .models import Annoncements

# Register your models here.
@admin.register(Annoncements)
class AnnoncementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'publish', 'status', 'description', 'image', 'seller_contact', 'category', 'created_at', 'updated_at')
    list_filter = ('user', 'publish', 'created_at')
    search_fields = ('name', 'price', 'location', 'description', 'seller_contact', 'category')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'created_at'
    ordering = ('publish', 'created_at')