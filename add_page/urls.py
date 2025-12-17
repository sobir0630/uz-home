from django.urls import path
from .views import add_announcement
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('add_announcement/', add_announcement, name='add_announcement'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
