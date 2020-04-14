from django.test import SimpleTestCase
from django.urls import reverse,resolve
from accounts.views import register,login,logout,passwordResetEmail,passwordResetEmailSent,passwordResetDone,passwordReset

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url=reverse('register')
        self.assertEqual(resolve(url).func,register)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,login)
    
    def test_logout_url_is_resolved(self):
        url=reverse('logout')
        self.assertEqual(resolve(url).func,logout)
    
    def test_password_reset_email_url_is_resolved(self):
        url=reverse('password_reset_email')
        self.assertEqual(resolve(url).func,passwordResetEmail)
    
    def test_password_reset_email_done_url_is_resolved(self):
        url=reverse('password_reset_email_done')
        self.assertEqual(resolve(url).func,passwordResetEmailSent)
    
    def test_password_reset_done_url_is_resolved(self):
        url=reverse('password_reset_done')
        self.assertEqual(resolve(url).func,passwordResetDone)
    
    def test_password_reset_url_is_resolved(self):
        url=reverse('password_reset',args={'token':"eehrtdvdssaxctey"})
        self.assertEqual(resolve(url).func,passwordReset)
