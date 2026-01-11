# users/signals.py
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def update_last_login(sender, user, request, **kwargs):
    user.last_login = timezone.now()
    user.save()
