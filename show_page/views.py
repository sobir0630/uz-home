from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
# email
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from add_page.models import Annoncements
from add_page.form import AnnoncementsForm
from .services import get_posts, get_image
from .forms import EmailSendForm
from users.models import User



class PostsView(View):
    def get(self, request):
        # Faqat published postlar
        elonlar = Annoncements.objects.filter(status='published').order_by('-created_at')

        # SEARCH
        search_query = request.GET.get('search', '')
        if search_query:
            elonlar = elonlar.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(location__icontains=search_query)
            )

        # CATEGORY FILTER
        selected_category = request.GET.get('category', '')
        if selected_category:
            elonlar = elonlar.filter(category=selected_category)

        # LOCATION FILTER
        location = request.GET.get('location', '')
        if location:
            elonlar = elonlar.filter(location__icontains=location)

        # PRICE FILTER
        min_price = request.GET.get('min_price', '')
        max_price = request.GET.get('max_price', '')

        try:
            if min_price:
                elonlar = elonlar.filter(price__gte=int(min_price))
            if max_price:
                elonlar = elonlar.filter(price__lte=int(max_price))
        except ValueError:
            pass  # Agar string kelib qoldi bo‘lsa, filter ishlamaydi

        # PAGINATION — 6ta post bir sahifa
        paginator = Paginator(elonlar, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # CONTEXT
        ctx = {
            'page_obj': page_obj,  # sahifalangan postlar
            'search_query': search_query,
            'selected_category': selected_category,
            'location': location,
            'min_price': min_price,
            'max_price': max_price,
            'category': Annoncements.HOME_CATEGORY_CHOICES,  # template bilan mos
        }
        return render(request, 'show/show_ann.html', ctx)


class PostsDetail(View):
    """
    Tanlangan postni ko'rsatadi va related posts (3 ta) chiqaradi.
    """

    def get(self, request, slug):
        # Tanlangan postni olish
        post = get_object_or_404(Annoncements, slug=slug)
        
        # Related posts: faqat category va location asosida, holati published
        related_posts = Annoncements.objects.filter(
            location=post.location,
            status='published'
        ).exclude(id=post.id)[:3]
        related_posts_list = list(related_posts)
        print('uxshash:', related_posts)
        print("related posts:", related_posts_list)
        
        context = {
            'post': post,
            'related_posts': related_posts
        }

        return render(request, 'show/detail.html', context)
    
# email
def detail_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail_page.html', {'post': post})


def send_email_form(request, pk):
    """
    Ushbu view:
    - Tanlangan postni oladi (pk orqali)
    - Email yuborish formasini ko‘rsatadi
    - Form to‘g‘ri bo‘lsa email yuboradi
    - Post detail sahifasining to‘liq URLini avtomatik hosil qiladi
    """

    # 1️⃣ Tanlangan postni olish
    post = get_object_or_404(Annoncements, pk=pk)

    sent = False  # Email yuborildi flag
    detail_url = request.build_absolute_uri(
        reverse('detail_page', kwargs={'slug': post.slug})
    )

    # 2️⃣ Agar POST bo‘lsa formni qayta ishlash
    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            # 3️⃣ Email yuborish
            send_mail(
                subject=form.cleaned_data['subject'],
                message=f"""
📌 {post.name}

📝 {post.description}

💰 Narxi: {post.price if post.price else 'Noma'}

🔗 Postni ko‘rish: {detail_url}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['to_email']],
                fail_silently=False
            )
            sent = True  # Email muvaffaqiyatli yuborildi

    # 4️⃣ Agar GET bo‘lsa yoki POST noto‘g‘ri bo‘lsa, formni ko‘rsatish
    else:
        form = EmailSendForm()

    # 5️⃣ Context tayyorlash
    context = {
        'post': post,
        'form': form,
        'sent': sent,
        'detail_url': detail_url,
    }

    # 6️⃣ HTML sahifaga render qilish
    return render(request, 'chat/send_email.html', context)


    
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
        print("account phone:", user.id)
        my_posts = Annoncements.objects.filter(user=user)
        

        ctx = {
            'user': user,
            'my_posts': my_posts
        }
        return render(request, 'get_logins/account.html', ctx)
    

class EditProfile(LoginRequiredMixin, View):

    def get(self, request):
        # Formani ko‘rsatish
        return render(request, 'get_logins/edit_profile.html')

    def post(self, request):
        queryset = User.objects,all()
        # Ma’lumotlarni saqlash
        user = request.user

        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.telegram = request.POST.get('telegram')

        user.save()
        return redirect('account')


class TogglePostStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(
            Annoncements,
            pk=pk,
            user=request.user  # faqat o‘z eloni
        )

        if post.status == 'draft':
            post.status = 'published'
        else:
            post.status = 'draft'

        post.save()
        return redirect('account')  # account sahifaga qaytadi