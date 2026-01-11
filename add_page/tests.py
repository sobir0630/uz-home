from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.text import slugify
from datetime import datetime
from .models import Annoncements


User = get_user_model()

class AddAnnouncementTest(TestCase):

    def setUp(self):
        # Test user yaratish
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # E'lon qo'shish URL
        self.add_url = reverse('add_announcement')

    def test_login_required(self):
        """Login qilinmagan user e'lon qo'sha olmasligi kerak"""
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 302)  # redirect login page

    # def test_add_announcement_success(self):
    #     """Login qilingan user e'lon qo'sha olishi kerak"""
    #     self.client.login(username='testuser', password='testpass123')
    #
    #     # test image
    #     image = SimpleUploadedFile(
    #         name='test_image.jpg',
    #         content=b'\x47\x49\x46\x38\x39\x61\x02\x00\x01\x00\x80\x00',
    #         content_type='image/jpeg'
    #     )
    #
    #     data = {
    #         'user': self.user.id,
    #         'name': 'Test eʼlon',
    #         'slug': '',
    #         'price': 1500000.00,
    #         'location': 'Toshkent',
    #         'description': 'Bu test uchun yozilgan eʼlon',
    #         'image': image,
    #         'seller_contact': '998901234567',
    #         'telegram': '@testuser',
    #         'category': 'house',
    #         'status': 'published',
    #     }
    #
    #     response = self.client.post(self.add_url, data, follow=True)
    #
    #     # redirect yoki success bo'lishi kerak
    #     self.assertEqual(response.status_code, 200)
    #
    #     # database da e'lon mavjudligini tekshirish
    #     self.assertEqual(Annoncements.objects.count(), 1)
    #     announcement = Annoncements.objects.first()
    #     self.assertEqual(announcement.name, 'Test eʼlon')
    #     self.assertEqual(announcement.user, self.user)
    #     self.assertEqual(announcement.slug, 'test-elon')
    #     self.assertEqual(announcement.category, 'house')
    #     self.assertEqual(announcement.status, 'published')
    #     self.assertTrue(announcement.image)  # image saqlanganligini tekshiradi

    def test_add_announcement_success(self):
        self.client.login(username='testuser', password='testpass123')

        with open('media/test/test.png', 'rb') as f:
            image = SimpleUploadedFile('test.png', f.read(), content_type="image/png")

        data = {
            'name': 'Test elon',
            'price': 1500000.00,
            'location': 'Toshkent',
            'description': 'Bu test uchun yozilgan eʼlon',
            'image': image,
            'seller_contact': '998901234567',
            'telegram': '@testuser',
            'category': 'house',
            'status': 'published',
        }

        response = self.client.post(self.add_url, data, follow=True)
        self.assertEqual(response.status_code, 200)

        # bazada e'lon mavjudligini tekshirish
        self.assertEqual(Annoncements.objects.count(), 1)
        announcement = Annoncements.objects.first()
        self.assertEqual(announcement.name, 'Test elon')
        self.assertEqual(announcement.user, self.user)