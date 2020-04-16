from django.test import TestCase,Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from accounts.models import User
from users.models import UserExtraDetails
import os


class TestView(TestCase):
    def setUp(self):
        self.client=Client()
        self.user = User.objects.create_user(username="username",email="email",password="password1",first_name="first_name",last_name="last_name")
        self.userdetails = UserExtraDetails(user_id=self.user.id).save()

        os.environ['MY_ID'] = 'username'
        self.index_url=reverse('index')
    
    def test_index_GET(self):
        print(self.index_url)
        response = self.client.get(self.index_url)
        print(response.content)
        self.assertEqual(response.status_code,200)
    
    def test_projects_GET(self):
        response = self.client.get(reverse('projects'))
        print(response.content)
        self.assertEqual(response.status_code,200)

