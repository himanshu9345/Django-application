from django import forms
from .models import UserExtraDetails
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm

class UserExtraDetailsForm(ModelForm):
    
    class Meta:
        model=UserExtraDetails
        fields=('user_interest','user_address','user_project_completed','user_image','user_resume')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_interest'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_user_interest)'})
        self.fields['user_address'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_user_address)'})
        self.fields['user_project_completed'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_user_project_completed)'})
        self.fields['user_image'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_user_image)'})
        self.fields['user_resume'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_user_resume)'})


    # def save(self, user,profile):
    #     obj = super(UserExtraDetailsForm,self).save(commit = False)
    #     obj.user = user
    #     obj.id=profile.id
    #     # obj.save()
    #     return obj

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email' )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_first_name)'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_last_name)'})
        self.fields['username'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_username)'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','onClick':'myFunction()','readonly':'readonly','oninput':'checkInputChanged(id_email)'})
    
