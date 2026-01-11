from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class UserFunctionalityTest(TestCase):
    def setUp(self):
        # Oddiy user
        self.user = User.objects.create_user(
            username="testuser",
            password="sha256",
            email="test@example.com",
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        # Superuser
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="adminpass",
            email="admin@example.com"
        )

    # -------------------------------
    # LOGIN TEST
    # -------------------------------
    def test_login_success(self):
        login = self.client.login(username="testuser", password="sha256")
        self.assertTrue(login)

    def test_login_fail_wrong_password(self):
        login = self.client.login(username="testuser", password="wrongpass")
        self.assertFalse(login)

    def test_login_fail_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        login = self.client.login(username="testuser", password="sha256")
        self.assertFalse(login)

    # -------------------------------
    # LOGOUT TEST
    # -------------------------------
    def test_logout(self):
        self.client.login(username="testuser", password="sha256")
        response = self.client.get(reverse("logout"))  # Agar logout URL bo‘lsa
        self.assertEqual(response.status_code, 302)   # Redirect bo‘lishi kerak

    # -------------------------------
    # CREATE / READ TEST
    # -------------------------------
    def test_user_created(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 2)  # testuser + admin

    def test_user_details(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    # -------------------------------
    # UPDATE TEST
    # -------------------------------
    def test_user_update(self):
        self.user.email = "newemail@example.com"
        self.user.is_staff = True
        self.user.save()

        updated_user = User.objects.get(username="testuser")
        self.assertEqual(updated_user.email, "newemail@example.com")
        self.assertTrue(updated_user.is_staff)

    # -------------------------------
    # DELETE TEST
    # -------------------------------
    def test_user_delete(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="testuser")

    # -------------------------------
    # SUPERUSER / STAFF TEST
    # -------------------------------
    def test_superuser_properties(self):
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_active)
