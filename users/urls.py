
from django.urls import path
from .views import home_page, get_login, register, get_logout

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', get_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', get_logout, name='logout'),
 ]
