from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # UserAdmin.fieldsets bilan birga qo‘shimcha maydonlarni qo‘shamiz
    fieldsets = UserAdmin.fieldsets + (
        ('Qo‘shimcha maʼlumot', {'fields': ('phone', 'telegram')}),
    )

    list_display = ('username', 'email', 'phone', 'telegram', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone', 'telegram')
    readonly_fields = ('date_joined',)