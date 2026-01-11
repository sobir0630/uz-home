from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from add_page.models import Annoncements
from django.utils import timezone

User = get_user_model()


class ShowAnnouncementTests(TestCase):

    def setUp(self):
        # user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # elonlar
        self.announcement1 = Annoncements.objects.create(
            user=self.user,
            name='Uy sotiladi',
            price=1500000,
            location='Toshkent',
            description='Yangi uy',
            telegram='@testuser',
            category='house',
            status='published',
            publish=timezone.now()
        )

        self.announcement2 = Annoncements.objects.create(
            user=self.user,
            name='Kvartira sotiladi',
            price=2000000,
            location='Samarqand',
            description='Zo‘r kvartira',
            telegram='@testuser',
            category='house',
            status='published',
            publish=timezone.now()
        )

        self.url = reverse('show_page')

    # 1️⃣ Sahifa ochiladimi
    def test_show_page_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    # 2️⃣ To‘g‘ri template ishlatilganmi
    def test_show_page_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'show/show_ann.html')

    # 3️⃣ Contextda barcha e’lonlar bormi
    def test_show_page_contains_announcements(self):
        response = self.client.get(self.url)
        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 2)

    # 4️⃣ E’lon nomlari sahifada ko‘rinayaptimi
    def test_show_page_content(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'Uy sotiladi')
        self.assertContains(response, 'Kvartira sotiladi')
