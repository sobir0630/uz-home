from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .form import UserSave
from .models import User



def log(request):
    user = get_object_or_404(User, id=1)
    html = f"<h1>Salom, bu users ilovasi {user.first_name}</h1>"
    return HttpResponse(html)


# Create your views here.
def home_page(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'main.html')


def get_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(User, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # login qilish
            messages.success(request, "Successfully logged in")
            return redirect("home_page")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'get_logins/login.html')

def register(request):
    if request.method == "POST":
        form = UserSave(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, "Successfully registered!")
            return redirect("home_page")
        else:
            messages.error(request, "Please correct the errors below")
    else:
        form = UserSave()  # POST bolmasa bo‘sh form

    return render(request, 'get_logins/register.html', {'form': form})

























