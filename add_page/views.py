
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import AnnoncementsForm
from .models import Annoncements
from users.models import User



@login_required
def add_announcement(request):
    catigories = Annoncements.HOME_CATEGORY_CHOICES

    if request.method == "POST":
        form = AnnoncementsForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)  # vaqtincha saqlaymiz, foydalanuvchini qo'shish uchun
            print(f"DEBUG: User ID = {request.user.id}")
            print(f"DEBUG: Username = {request.user.username}")
            print(f"DEBUG: Is authenticated = {request.user.is_authenticated}")
            
            # Foydalanuvchini belgilaymiz
            new_post.user = request.user

            # Saqlashdan oldin barcha maydnlarni tekshiramiz
            print(f"DEBUG: Post title = {new_post.name}")
            print(f"DEBUG: Post price = {new_post.price}")
            print(f"DEBUG: Post user = {new_post.user}")
            
            new_post.save()               # bazaga saqlaymiz
            messages.success(request, "E'lon muvaffaqiyatli qo'shildi")
            return redirect('home_page')
        else:
            messages.error(request, """Formani to'ldirishda xatolik yuz berdi.
                                      Har bir qatorni to'liq tekshirib, qayta urinib ko'ring.""")
    else:
        form = AnnoncementsForm()

    # return render(request, 'add/add_ann.html', {'form': form, 'catigories': catigories, 'status': Annoncements.STATUS_CHOISES})
    return render(request, 'add/add_ann.html' , {'form': form})