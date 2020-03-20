from django import forms
from .models import UserExtraDetails
from django.forms import ModelForm

class UserForm(ModelForm):
    
    class Meta:
        model=UserExtraDetails
        exclude=('user','user_image','user_resume')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_interest'].widget.attrs.update({'class': 'form-control'})
        self.fields['user_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['user_project_completed'].widget.attrs.update({'class': 'form-control'})

    def save(self, user,id):
        obj = super().save(commit = False)
        obj.user = user
        obj.id=id
        obj.save()
        return obj