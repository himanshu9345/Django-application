from django import forms
from .models import UserExtraDetails

class UserForm(forms.Form):
    # first_name = forms.CharField(label='First Name', max_length=100)
    # last_name = forms.CharField(label='Last Name', max_length=100)
    user_image = forms.ImageField()
    user_intrest = forms.CharField(max_length=400)
    user_address = forms.CharField(max_length=200)
    user_resume = forms.FileField() 
    user_project_completed = forms.IntegerField()
    # user_id=forms.IntegerField()

    class Meta:
        model=UserExtraDetails

