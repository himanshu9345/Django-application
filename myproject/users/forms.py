from django import forms
from .models import UserExtraDetails,Experience,Education,Award,Skill,Publication,Project,ContactDetails
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm

class UserExtraDetailsForm(ModelForm):
    
    class Meta:
        model=UserExtraDetails
        
        fields=('user_interest','user_address','user_project_completed','user_image','user_resume')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_interest'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_user_interest)'})
        self.fields['user_address'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_user_address)'})
        self.fields['user_project_completed'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_user_project_completed)'})
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

class DateInput(forms.DateInput):
    input_type='date' 
class ExperienceForm(ModelForm):
    
    class Meta:
        model=Experience
        fields=('company','position','desc','start_month_year','end_month_year')
        widgets = {
            'start_month_year': DateInput(),
            'end_month_year': DateInput(),
        }
        labels = {
            'desc': 'Description (every bullet point add # in the end)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_company)'})
        self.fields['position'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_position)'})
        self.fields['desc'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_desc)','placeholder': 'I increase the ..... output by 40%.# Worked with ....... teams.# Develop XYZ module ...... helped team.# dont forget to add # in the end for every bullet point.'})
        self.fields['start_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_start_month_year)'})
        self.fields['end_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_end_month_year)'})

class EducationForm(ModelForm):
    
    class Meta:
        model=Education
        fields=('college_name','degree_name','major_name','college_start_month_year','college_end_month_year')
        widgets = {
            'college_start_month_year': DateInput(),
            'college_end_month_year': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['college_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_college_name)'})
        self.fields['degree_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_degree_name)'})
        self.fields['major_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_major_name)'})
        self.fields['college_start_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_college_start_month_year)'})
        self.fields['college_end_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_college_end_month_year)'})

class AwardForm(ModelForm):
    
    class Meta:
        model=Award
        fields=('award_name','award_place','describe_award','award_month_year')
        widgets = {
            'award_month_year': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['award_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_award_name)'})
        self.fields['award_place'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_award_place)'})
        self.fields['describe_award'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_describe_award)'})
        self.fields['award_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_award_month_year)'})

class SkillForm(ModelForm):
    
    class Meta:
        model=Skill
        fields=('skill_name','percentage_you_know')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skill_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_skill_name)'})
        self.fields['percentage_you_know'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_percentage_you_know)'})

class PublicationForm(ModelForm):
    
    class Meta:
        model=Publication
        fields=('publication_title','publication_name','publication_date','publication_url','publication_description')
        widgets = {
            'publication_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['publication_title'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_publication_title)'})
        self.fields['publication_name'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_publication_name)'})
        self.fields['publication_date'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_publication_date)'})
        self.fields['publication_url'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_publication_url)'})
        self.fields['publication_description'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_publication_description)'})

class ProjectForm(ModelForm):
    
    class Meta:
        model=Project
        fields=('project_title','project_description','project_url','project_image','project_start_month_year','project_end_month_year')
        widgets = {
            'project_start_month_year': DateInput(),
            'project_end_month_year': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project_title'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_title)'})
        self.fields['project_description'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_description)'})
        self.fields['project_url'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_url)'})
        self.fields['project_image'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_image)'})
        self.fields['project_start_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_start_month_year)'})
        self.fields['project_end_month_year'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_project_end_month_year)'})

class ContactDetailsForm(ModelForm):
    
    class Meta:
        model=ContactDetails
        fields=('contact_type','contact_profile_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact_type'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_contact_type)'})
        self.fields['contact_profile_url'].widget.attrs.update({'class': 'form-control','oninput':'checkInputChanged(id_contact_profile_url)'})