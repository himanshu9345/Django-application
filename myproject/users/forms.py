from django import forms
from .models import UserExtraDetails

class UserForm(forms.Form):
    class Meta:
        model=UserExtraDetails
        fields=[
            'user_intrest',
            'user_address',
            'user_project_completed'
        ]

