from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.statuses.models import Status
from task_manager.apps.users.models import User


class StatusCRUDTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client = Client()
        self.client.login(username="testuser", password="testpassword")
        self.status = Status.objects.create(name="teststatus")

    def test_status_list_view(self):
        response = self.client.get(reverse_lazy("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/statuses.html")

    def test_create_status_view(self):
        response = self.client.post(
            reverse_lazy("create_status"), data={"name": "New status"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name="New status").exists())

    def test_status_update_view(self):
        response = self.client.post(
            reverse_lazy("update_status", kwargs={"pk": self.status.pk}),
            data={"name": "Updated status"},
        )
        self.assertEqual(response.status_code, 302)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, "Updated status")

    def test_status_delete_view(self):
        response = self.client.post(
            reverse_lazy("delete_status", kwargs={"pk": self.status.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())
