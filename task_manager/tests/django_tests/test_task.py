from django.test import TestCase, Client
from django.urls import reverse_lazy

from task_manager.apps.tasks.models import Task
from task_manager.apps.users.models import User
from task_manager.apps.statuses.models import Status


class TaskCRUDTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="testuser")
        self.user.set_password("testpassword")
        self.user.save()
        self.client.login(username="testuser", password="testpassword")
        self.status = Status.objects.create(name="teststatus")
        self.task = Task.objects.create(name="testtask", description="testdescription", author=self.user, executor=self.user, status=self.status)

    def test_create_task(self):
        response = self.client.post(reverse_lazy("create_task"), data={
            "name": "New task",
            "description": "Test description",
            "author": self.user.pk,
            "executor": self.user.pk,
            "status": self.status.pk}
            )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name="New task").exists())

    def test_update_task(self):
        response = self.client.post(reverse_lazy("update_task", kwargs={"pk": self.task.pk}), data={"name": "Updated task"})
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(Task.objects.filter(name="Updated task").exists())

    def test_delete_task(self):
        response = self.client.post(reverse_lazy("delete_task", kwargs={"pk": self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())