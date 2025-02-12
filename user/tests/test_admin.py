from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


from user.models import User
from user.admin import UserAdmin


class MockRequest:
    pass


class UserAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = UserAdmin(User, self.site)
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password",
            first_name="Test",
            last_name="User",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )
        self.request = MockRequest()

    def test_fieldsets(self):
        fieldsets = self.admin.get_fieldsets(self.request, obj=self.user)
        self.assertEqual(
            fieldsets,
            (
                (None, {"fields": ("email", "password")}),
                (_("Personal info"), {"fields": ("first_name", "last_name")}),
                (
                    _("Permissions"),
                    {
                        "fields": (
                            "is_active",
                            "is_staff",
                            "is_superuser",
                            "groups",
                            "user_permissions",
                        )
                    },
                ),
                (_("Important dates"), {"fields": ("last_login", "date_joined")}),
            ),
        )

    def test_add_fieldsets(self):
        add_fieldsets = self.admin.add_fieldsets
        self.assertEqual(
            add_fieldsets,
            (
                (
                    None,
                    {
                        "classes": ("wide",),
                        "fields": ("email", "password1", "password2"),
                    },
                ),
            ),
        )

    def test_list_display(self):
        self.assertEqual(
            self.admin.list_display, ("email", "first_name", "last_name", "is_staff")
        )

    def test_search_fields(self):
        self.assertEqual(self.admin.search_fields, ("email", "first_name", "last_name"))

    def test_ordering(self):
        self.assertEqual(self.admin.ordering, ("email",))

    def test_user_change(self):
        self.client.login(email="testuser@example.com", password="password")
        url = reverse(
            f"admin:{self.user._meta.app_label}_{self.user._meta.model_name}_change",
            args=[self.user.pk],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
