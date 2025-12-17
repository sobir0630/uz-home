from django.shortcuts import render
from django.contrib import messages
from .models import ShowPage



# Create your views here.
def show_page(request):
    """View function for displaying the show page."""
    if request.method == "GET":
        posts = ShowPage.objects.all().order_by('-created_at') # yangi elonlar birinchi
        return render(request, "show/show_ann.html", {"posts": posts})
    else:
        messages.error(request, "Noma'lum so'rov turi")

    return render(request, "show/show_ann.html")