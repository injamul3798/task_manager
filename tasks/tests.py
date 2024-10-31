from django.test import TestCase
from .models import Task
from django.urls import reverse

class TaskModelTest(TestCase):
    
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="This is a test task", completed=False)

    def test_task_creation(self):
        """Test creating a task with valid data."""
        task = Task.objects.create(title="New Task", description="New description", completed=False)
        self.assertEqual(task.title, "New Task")
        self.assertEqual(task.description, "New description")
        self.assertFalse(task.completed)

    def test_task_creation_without_title(self):
        """Test creating a task without a title."""
        with self.assertRaises(ValueError):
            Task.objects.create(description="Missing title")

    def test_task_retrieval(self):
        """Test retrieving a task by ID."""
        retrieved_task = Task.objects.get(id=self.task.id)
        self.assertEqual(retrieved_task.title, self.task.title)

    def test_task_update(self):
        """Test updating a task's details."""
        self.task.title = "Updated Task"
        self.task.save()
        self.assertEqual(Task.objects.get(id=self.task.id).title, "Updated Task")

    def test_mark_task_as_completed(self):
        """Test marking a task as completed."""
        self.task.completed = True
        self.task.save()
        self.assertTrue(Task.objects.get(id=self.task.id).completed)

    def test_task_deletion(self):
        """Test deleting a task."""
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)

    def test_delete_non_existent_task(self):
        """Test attempting to delete a non-existent task."""
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=9999).delete()

    def test_retrieve_all_tasks(self):
        """Test retrieving all tasks."""
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 1)  # Expecting 1 task in the database initially

    def test_retrieve_completed_tasks(self):
        """Test retrieving only completed tasks."""
        self.task.completed = True
        self.task.save()
        completed_tasks = Task.objects.filter(completed=True)
        self.assertEqual(completed_tasks.count(), 1)

    def test_error_handling_invalid_id(self):
        """Test how the system responds to an invalid ID."""
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=9999)

    def test_empty_task_list(self):
        """Test handling of an empty task list."""
        Task.objects.all().delete()  # Delete the existing task
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 0)

    def test_task_update_invalid_data(self):
        """Test updating a task with invalid data (e.g., missing title)."""
        self.task.title = ""
        with self.assertRaises(ValueError):
            self.task.save()
