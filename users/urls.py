
from django.urls import path
from .views import home_page, get_login, register, get_logout
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', get_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', get_logout, name='logout'),
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
