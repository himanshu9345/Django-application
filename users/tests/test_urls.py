from django.test import SimpleTestCase
from django.urls import reverse,resolve
from users.views import index,projects,sendemail,userProjects,deleteCategory,editableCategory,showCategory,viewProfile,showEditableProfile

class TestUrls(SimpleTestCase):
    
    def test_index_url_is_resolved(self):
        url=reverse('index')
        self.assertEqual(resolve(url).func,index)

    def test_projects_url_is_resolved(self):
        url=reverse('projects')
        self.assertEqual(resolve(url).func,projects)
    
    def test_profile_url_is_resolved(self):
        url=reverse('profile')
        self.assertEqual(resolve(url).func,showEditableProfile)
    
    def test_viewprofile_url_is_resolved(self):
        url=reverse('viewprofile', args={'username':"himanshu"})
        self.assertEqual(resolve(url).func,viewProfile)

    def test_sendemail_url_is_resolved(self):
        url=reverse('sendemail', args={'username':"himanshu"})
        self.assertEqual(resolve(url).func,sendemail)
    
    def test_userprojects_url_is_resolved(self):
        url=reverse('userprojects', args={'username':"himanshu"})
        self.assertEqual(resolve(url).func,userProjects)
    
    def test_deletecategory_url_is_resolved(self):
        url=reverse('deletecategory', args={'category':"experience",'category_id':'1'})
        self.assertEqual(resolve(url).func,deleteCategory)
    
    def test_editablecategory_url_is_resolved(self):
        url=reverse('editablecategory', args={'category':"experience",'category_id':'1'})
        self.assertEqual(resolve(url).func,editableCategory)
    
    # def test_category_url_is_resolved(self):
    #     url=reverse('category', args={'category':"experience"})
    #     self.assertEqual(resolve(url).func,showCategory)