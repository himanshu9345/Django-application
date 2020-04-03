from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import index,projects

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url=reverse('index')
        self.assertEqual(resolve(url).func,index)

    def test_projects_url_is_resolved(self):
        url=reverse('projects')
        self.assertEqual(resolve(url).func,projects)