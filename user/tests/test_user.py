from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


class UserManagerTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "test@example.com"
        password = "testpass123"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@EXAMPLE.COM"
        user = User.objects.create_user(email, "testpass123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(None, "testpass123")

    def test_create_superuser(self):
        email = "superuser@example.com"
        password = "superpass123"
        user = User.objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_duplicate_email(self):
        email = "test@example.com"
        User.objects.create_user(email=email, password="testpass123")
        with self.assertRaises(IntegrityError):
            User.objects.create_user(email=email, password="testpass123")


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = "testuser@example.com"
        password = "password123"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_without_username(self):
        email = "testuser2@example.com"
        password = "password123"
        user = User.objects.create_user(email=email, password=password)

        self.assertIsNone(user.username)
