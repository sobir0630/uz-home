from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from . import services
from .form import UserSave
from add_page.models import Annoncements
from django.contrib.auth import get_user_model


User = get_user_model()
# -----------------------
#----- REGISTER ---------
# -----------------------
# Decorator
def login_required_decorator(view_func):
    return login_required(view_func, login_url='login')


# Login
def get_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Faqat username va password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # login qiladi
            messages.success(request, "Successfully logged in")
            return redirect("home_page")
        else:
            messages.error(request, "Invalid username or password | ")


    return render(request, 'get_logins/login.html')



# Register
def register(request):
    if request.method == "POST":
        form = UserSave(request.POST)
        if form.is_valid(): 
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            messages.success(request, "Successfully registered!")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = UserSave()  

    return render(request, 'get_logins/register.html', {'form': form})


# Logout
@login_required_decorator
def get_logout(request):
    logout(request)
    return redirect('login')


# Home page
# @login_required
def home_page(request):
    posts = Annoncements.objects.filter(status='published').order_by('-created_at')
    username = request.user.username
    print(f"DEBUG: Username = {username}")
    catigories = Annoncements.HOME_CATEGORY_CHOICES
    
    # Paginator
    paginator = Paginator(posts, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    ctx = {
        'page_obj': page_obj,
        'catigories': catigories,
        'username': username,
           
    }
    
    return render(request, 'main.html', ctx)

