from django.test import TestCase,Client
from django.test.utils import setup_test_environment
from django.urls import reverse


# class TestView(TestCase):
    
#     def setUp(self):
#         self.client=Client()
#         self.index_url=reverse('index')
    
#     def test_index_GET(self):
#         print(self.index_url)
#         response = self.client.get(self.index_url)
#         print(response)
#         self.assertEqual(response.status_code,200)
#         self.assserTemplateUsed(response,'userprofile.html')

