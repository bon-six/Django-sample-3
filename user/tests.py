from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

user_model = get_user_model()

class UserModelTests(TestCase):
    def setUp(self):
        testuser1 = user_model.objects.create_user(email='test1@example.com',password='testuser1234')
        testuser1.save()
        testuser2 = user_model.objects.create_superuser(email='admin@example.com',password='testuser1234')
        testuser2.save()
        testuser3 = user_model.objects.create_staffuser(email='test2@example.com',password='testuser1234')
        testuser3.save()

    def test_user_login(self):
        res = self.client.login(email='admin@example.com',password='testuser1234')
        self.assertTrue(res)
        res = self.client.login(email='test1@example.com',password='testuser1234')
        self.assertTrue(res)
        res = self.client.login(email='test2@example.com',password='testuser1234')
        self.assertTrue(res)