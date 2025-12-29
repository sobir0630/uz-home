from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from add_page.models import Annoncements
from add_page.form import AnnoncementsForm
from .services import get_posts, get_image


class PostsView(View):
       def get(self, request):
        elonlar = Annoncements.objects.all().order_by('-created_at')
        print('DEBUG:', elonlar)
        
        # defoult 5ta page
        paginator = Paginator(elonlar, 6)
        
        # page number
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # search
        search = request.GET.get('search')
        if search:
            elonlar = elonlar.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(location__icontains=search)
            )

        # category
        category = request.GET.get('category')
        if category:
            elonlar = elonlar.filter(category=category)
            
        location = request.GET.get('location')
        if location:
            elonlar = elonlar.filter(location__icontains=location)

        min_price = request.GET.get('min_price')
        if min_price:
            elonlar = elonlar.filter(price__gte=min_price)

        max_price = request.GET.get('max_price')
        if max_price:
            elonlar = elonlar.filter(price__lte=max_price)

        ctx = {
            'posts': elonlar,
            'page_obj': page_obj,
            'search_query': search,
            'selected_category': category,
            'location': location,
            'min_price': min_price,
            'max_price': max_price,
            'category': Annoncements.HOME_CATEGORY_CHOICES,
        }
        return render(request, 'show/show_ann.html', ctx)


class PostsDetail(View):
    def get(self, request, slug):
        posts = get_object_or_404(Annoncements, slug=slug)
        print("DEBUG Detail:", posts)
        print("DEBUG Detail:", posts.telegram)
        
        releted_posts = Annoncements.objects.filter(
            category=posts.category,
            location=posts.location,
        ).exclude(id=posts.id)[:3]
        
        ctx = {
            'post': posts,
            'related_posts': releted_posts,
        }
        return render(request, "show/detail.html", ctx)
    
class PostUpdateView(UpdateView):
    model = Annoncements
    form_class = AnnoncementsForm
    template_name = 'edit/edit.html'  # tahrirlash sahifasi
    pk_url_kwarg = 'pk'  # URL da pk parametri bo‘lsa
    context_object_name = 'post'

    def get_success_url(self):
        # o‘zgartirishdan keyin qaysi sahifaga qaytadi
        return reverse_lazy('show_page')
 
class PostDelete(DeleteView):
    model = Annoncements
    template_name = "edit/delete.html"
    success_url = reverse_lazy('account')

class AccountView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        print("account phone:", user.email)
        my_posts = Annoncements.objects.filter(user=user)

        ctx = {
            'user': user,
            'my_posts': my_posts
        }
        return render(request, 'get_logins/account.html', ctx)