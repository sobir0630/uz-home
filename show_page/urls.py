from django.urls import path 
from .views import Posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('show_page/', Posts, name='show_page'),
]


