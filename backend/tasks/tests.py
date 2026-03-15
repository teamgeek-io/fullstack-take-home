from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskApiTests(APITestCase):
    def test_can_create_task(self):
        response = self.client.post(
            reverse("task-list-create"),
            {
                "title": "Write assignment docs",
                "description": "Create candidate instructions",
                "status": "todo",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Write assignment docs")
