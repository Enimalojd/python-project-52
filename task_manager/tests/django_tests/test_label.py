from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.labels.models import Label
from task_manager.apps.users.models import User


class LabelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client = Client()
        self.client.login(username="testuser", password="testpassword")
        self.label = Label.objects.create(name="testlabel")

    def test_label_list_view(self):
        response = self.client.get(reverse_lazy("labels"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels/labels.html")

    def test_create_label_view(self):
        response = self.client.post(
            reverse_lazy("create_label"), data={"name": "New label"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Label.objects.filter(name="New label").exists())

    def test_update_label_view(self):
        response = self.client.post(
            reverse_lazy("update_label", kwargs={"pk": self.label.pk}),
            data={"name": "Updated label"},
        )
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, "Updated label")

    def test_delete_label_view(self):
        response = self.client.post(
            reverse_lazy("delete_label", kwargs={"pk": self.label.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Label.objects.filter(pk=self.label.pk).exists())
