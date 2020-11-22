from django.test import TestCase,Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from accounts.models import User
from users.models import UserExtraDetails,Experience
import os


class TestView(TestCase):
    def setUp(self):
        self.client=Client()
        self.user = User.objects.create_user(username="test",email="test@email.com",password="password1",first_name="Test",last_name="User")
        self.experienceObject = Experience.objects.create(company="XYZ",position="ABC",desc="I am working on",end_month_year="2020-03-04",start_month_year="2020-03-04",user_id=self.user.id)
        self.userdetails = UserExtraDetails(user_id=self.user.id).save()
        self.loggedInClient=Client()
        self.loggedInClient.login(username=self.user.username,password="password1")
        os.environ['MY_ID'] = self.user.username
    
    def test_index_GET(self):
        # print(reverse('index'))
        response = self.client.get(reverse('index'))
        # print(response.content)
        self.assertEqual(response.status_code,200)
    
    def test_index_MY_ID_UserNotFound_GET(self):
        os.environ['MY_ID'] = "TestUserNotFound"
        # print(reverse('index'))
        response = self.client.get(reverse('index'))
        # print(response.content)
        self.assertEqual(response.status_code,404)
        os.environ['MY_ID'] = self.user.username

    
    def test_projects_GET(self):
        response = self.client.get(reverse('projects'))
        # print(response.content)
        self.assertEqual(response.status_code,200)

    def test_profile_without_login_GET(self):
        response = self.client.get(reverse('profile'))
        # print(response.url)
        self.assertEqual(response.status_code,302)
        self.assertURLEqual(response.url,"/accounts/login/?next=/profile/")

    def test_profile_with_login_GET(self):
        response = self.loggedInClient.get(reverse('profile'))
        print(response.context)
        self.assertEqual(response.status_code,200)

    def test_userProfile_GET(self):
        response = self.client.get(reverse('viewprofile', args={"test"}))
        self.assertEqual(response.status_code,200)
    
    def test_userProfile_NotFound_GET(self):
        response = self.client.get(reverse('viewprofile', args={"TestUserNotFound"}))
        self.assertEqual(response.status_code,404)
    
    def test_userProjects_GET(self):
        response = self.client.get(reverse('userprojects', args={"test"}))
        self.assertEqual(response.status_code,200)
    
    def test_userProjects_NotFound_GET(self):
        response = self.client.get(reverse('userprojects', args={"TestUserNotFound"}))
        self.assertEqual(response.status_code,404)
    
    # def test_editableCategory_GET(self):
    #     response = self.loggedInClient.get(reverse('editablecategory', args={"test","experience"}))
    #     self.assertEqual(response.status_code,200)
    def test_showCategory_GET(self):
        response = self.loggedInClient.get(reverse('category', args={"experience"}))
        self.assertEqual(response.status_code,200)
    
    def test_showCategory_NotFount_GET(self):
        response = self.loggedInClient.get(reverse('category', args={"experiences"}))
        self.assertEqual(response.status_code,404)
    
    def test_editableCategory_GET(self):
        response = self.loggedInClient.get(reverse('editablecategory', kwargs={'category':"experience",'category_id':"new"}))
        self.assertEqual(response.status_code,200)
    
    def test_editableCategory_oldObject_GET(self):
        response = self.loggedInClient.get(reverse('editablecategory', kwargs={'category':"experience",'category_id':str(self.experienceObject.id)}))
        self.assertEqual(response.status_code,200)
    
    def test_editableCategory_createObject_POST(self):
        response = self.loggedInClient.post(reverse('editablecategory',kwargs={'category':"experience",'category_id':str(self.experienceObject.id)}))
        self.assertEqual(response.status_code,200)