from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.users.models import User


class UserTest(TestCase):

    registeration_data = {
        "first_name": "Test",
        "last_name": "User",
        "username": "testuser",
        "password1": "testpassword",
        "password2": "testpassword",
    }

    updated_data = {
        "first_name": "Updated name",
        "last_name": "Updated surname",
        "username": "testuser",
        "password1": "testpassword",
        "password2": "testpassword",
    }

    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="baseuser")
        self.user.set_password("testpassword")
        self.user.save()

    def test_signup_page_view(self):
        response = self.client.get(reverse_lazy("create_user"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create_user.html")

    def test_create_user_view(self):
        response = self.client.post(
            reverse_lazy("create_user"), data=self.registeration_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_delete_user_view(self):
        self.assertTrue(User.objects.filter(username="baseuser").exists())
        user = User.objects.filter(username="baseuser").first()
        pk = user.pk
        response = self.client.post(reverse_lazy("delete_user", kwargs={"pk": pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(pk=pk).exists())

    def test_update_user_view(self):
        user = User.objects.filter(username="baseuser").first()
        pk = user.pk
        response = self.client.post(
            reverse_lazy("update_user", kwargs={"pk": pk}), data=self.updated_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(first_name="Updated name").exists())
