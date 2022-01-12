from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Task


user_model = get_user_model()
# Create your tests here.

class TaskModelTests(TestCase):
    def setUp(self):
        super().setUp()
        Task.objects.create(
            title='first task',
            description='task details',
            pub_date=timezone.now().date(),
            due_date=timezone.now().date()+timedelta(days=3)
        )
    
    def test_task_in_db(self):
        t = Task.objects.get(pk=1)
        self.assertEqual(f'{t.title}', 'first task')
        self.assertEqual(f'{t.description}', 'task details')
        self.assertIsNone(t.manager)
        self.assertFalse(t.member.all())

    def test_m2m_relation(self):
        testuser1 = user_model.objects.create_user(email='test1@example.com',password='testuser1234')
        testuser1.save()
        testuser2 = user_model.objects.create_superuser(email='admin@example.com',password='testuser1234')
        testuser2.save()
        testuser3 = user_model.objects.create_staffuser(email='test2@example.com',password='testuser1234')
        testuser3.save()
        t = Task.objects.get(pk=1)
        t.manager=testuser1
        t.member.add(testuser2, testuser3)
        t.save()
        self.assertEqual(user_model.objects.get(pk=1).managing_tasks.get(), t)
        self.assertEqual(user_model.objects.get(pk=2).involving_tasks.all().count(),1)
        self.assertEqual(user_model.objects.get(pk=3).involving_tasks.get(),t)