from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.users.models import User


class MainTest(TestCase):

    login_data = {
        "username": "testuser",
        "password": "testpassword",
    }

    @classmethod
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username=self.login_data["username"])
        self.user.set_password(self.login_data["password"])
        self.user.save()

    def test_login_page(self):
        response = self.client.get(reverse_lazy("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/login.html")

    def test_login(self):
        response = self.client.post(reverse_lazy("login"), data=self.login_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("index"))
        self.assertTrue(
            self.client.login(
                username=self.login_data["username"],
                password=self.login_data["password"],
            )
        )
