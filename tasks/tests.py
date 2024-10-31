from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title="Test Task", description="This is a test task", completed=False)

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertFalse(task.completed)
