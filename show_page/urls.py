from django.urls import path 
from .views import show_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('show_page/', show_page, name='show_page'),
]


