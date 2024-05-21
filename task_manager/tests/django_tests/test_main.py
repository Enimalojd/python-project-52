from django.test import TestCase, Client
from django.urls import reverse_lazy


class MainTest(TestCase):

    @classmethod
    def setUp(self):
        self.client = Client()

    def test_main_page(self):
        response = self.client.get(reverse_lazy("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
    
    def test_users_page(self):
        response = self.client.get(reverse_lazy("users"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/users.html")

    def test_auth_page(self):
        response = self.client.get(reverse_lazy("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/login.html")
    
    def test_register_page(self):
        response = self.client.get(reverse_lazy("create_user"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create_user.html")

