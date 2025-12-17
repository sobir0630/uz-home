from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .form import annoncementsForm
from .models import annoncements
from users.models import User


def add_announcement(request):
    user_id = request.session.get('user_id')
    print("user", user_id)
    if not user_id:
        messages.info(request, "Iltimos, avval tizimga kiring")
        return redirect('login')

    user = User.objects.get(id=user_id)
    print(user)

    if request.method == "POST":
        form = annoncementsForm(request.POST, request.FILES)
        if form.is_valid():
            announcement = form.save(commit=False)  # bazaga saqlamaymiz
            announcement.user = user              # sessiondan olingan user
            announcement.save()                   # bazaga saqlaymiz
            messages.success(request, "E'lon muvaffaqiyatli qo'shildi")
            return redirect('home_page')
        else:
            messages.error(request, """Formani to'ldirishda xatolik yuz berdi.
                                        Har bir qatorni to'liq tekshirib, qayta urinib ko'ring.""")

    else:
        form = annoncementsForm()

    return render(request, 'add/add_ann.html', {'form': form})
