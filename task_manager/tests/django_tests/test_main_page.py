from django.test import TestCase, Client
from django.urls import reverse_lazy


class TestMainPage(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_main_page(self):
        response = self.guest_client.get(reverse_lazy('index'))
        self.assertEqual(response.status_code, 200)

    