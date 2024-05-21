from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.users.models import User


class UserTest(TestCase):

    register_data = {
        "first_name": "Test",
        "last_name": "User",
        "username": "testuser",
        "password1": "testpassword",
        "password2": "testpassword",
        }

    @classmethod
    def setUp(self):
        self.client = Client()

    def test_signup_page(self):
        response = self.client.get(reverse_lazy("create_user"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create_user.html")

    def test_create_user(self):
        response = self.client.post(reverse_lazy("create_user"), data=self.register_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertTrue(User.objects.filter(username="testuser").exists())
    
    def test_delete_user(self):
        response = self.client.post(reverse_lazy("delete_user"))
        self.assertEqual(response.status_code, 302)
        #TODO check if user is deleted
    
    def test_update_user(self):
        response = self.client.post(reverse_lazy("update_user"))
        self.assertEqual(response.status_code, 302)
        #TODO check if user is updated

