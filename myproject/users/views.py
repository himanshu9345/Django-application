from django.shortcuts import render,redirect
from .forms import UserExtraDetailsForm,UserForm,ExperienceForm,EducationForm,AwardForm
from django.contrib.auth.decorators import login_required
from .models import UserExtraDetails,Experience,Education,Award
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.

def viewprofile(request,user_id):
    print(request,"viewprofile")
    return render(request,"index.html",{'user_id':user_id})

def convertToCamelCase(word):
    return ' '.join(x.capitalize() or '_' for x in word.split('_'))

@login_required
def showAward(request):
    current_user_id=request.user.id
    user_awards=Award.objects.filter(user_id=current_user_id)
    fieldlist=[convertToCamelCase(f.name)  for f in Award._meta.get_fields() if f.name!='user']
    return render(request,"commondisplaypage.html",{'fieldlist':fieldlist,'user_forms':user_awards})

@login_required
def deleteAward(request,award_id):
    try:
        user_award= get_object_or_404(award, pk=exp_id)
        user_award.delete()
        return redirect('awards')

    except:
        raise Http404("No award found")


@login_required
def editableAward(request,award_id):
    current_user_id=request.user.id
    user_award_form=AwardForm()
    user_award_data=None
    if request.method=='POST':
        user_award=None
        if award_id!='new':
            user_award=Award.objects.filter(user_id=current_user_id,id=int(award_id))
        if user_award:
            user_award_data=user_award[0]
        
        if user_award or award_id=='new':
            user_award_form=AwardForm(data=request.POST,instance=user_award_data)
            obj=user_award_form.save(commit=False)
            
            if award_id=='new':
                obj.user_id=current_user_id
            obj.save()
            return redirect('awards')
        else:
            raise Http404("No experience found")
            
    else:
        if award_id!="new":
            user_award=Award.objects.filter(user_id=current_user_id,id=int(award_id))
            if user_award:
                user_award_data=user_award[0]
                user_award_form=AwardForm(instance=user_award_data)
                print(user_award_form)
            else:
                raise Http404("No award found")
    
    return render(request,"award.html",{'form_requested':user_education_form})



@login_required
def showEducation(request):
    current_user_id=request.user.id
    user_educations=Education.objects.filter(user_id=current_user_id)
    return render(request,"educations.html",{'user_educations':user_educations})

@login_required
def deleteEducation(request,education_id):
    try:
        user_education= get_object_or_404(Education, pk=exp_id)
        user_education.delete()
        return redirect('educations')

    except:
        raise Http404("No education found")


@login_required
def editableEducation(request,education_id):
    current_user_id=request.user.id
    user_education_form=EducationForm()
    user_education_data=None
    if request.method=='POST':
        user_education=None
        if education_id!='new':
            user_education=Education.objects.filter(user_id=current_user_id,id=int(education_id))
        if user_education:
            user_education_data=user_education[0]
        
        if user_education or education_id=='new':
            user_education_form=EducationForm(data=request.POST,instance=user_education_data)
            obj=user_education_form.save(commit=False)
            
            if education_id=='new':
                obj.user_id=current_user_id
            obj.save()
            return redirect('educations')
        else:
            raise Http404("No experience found")
            
    else:
        if education_id!="new":
            user_education=Education.objects.filter(user_id=current_user_id,id=int(education_id))
            if user_education:
                user_education_data=user_education[0]
                user_education_form=EducationForm(instance=user_education_data)
                print(user_education_form)
            else:
                raise Http404("No education found")
    
    return render(request,"education.html",{'user_education_form':user_education_form})


@login_required
def showExperience(request):
    current_user_id=request.user.id
    user_experiences=Experience.objects.filter(user_id=current_user_id)

    # print (exp_id)
    return render(request,"experiences.html",{'user_experiences':user_experiences})

@login_required
def deleteExperience(request,exp_id):
    try:
        user_experience= get_object_or_404(Experience, pk=exp_id)
        user_experience.delete()
        return redirect('experiences')

    except:
        raise Http404("No experience found")


@login_required
def editableExperience(request,exp_id):
    current_user_id=request.user.id
    user_experience_form=ExperienceForm()
    user_exp_data=None
    if request.method=='POST':
        try:
            user_experience=None
            if exp_id!='new':
                user_experience=Experience.objects.filter(user_id=current_user_id,id=int(exp_id))
            if user_experience:
                user_exp_data=user_experience[0]
                
            user_experience_form=ExperienceForm(data=request.POST,instance=user_exp_data)
            obj=user_experience_form.save(commit=False)
            
            if exp_id=='new':
                obj.user_id=current_user_id
            obj.save()
            return redirect('experiences')
        except:
            raise Http404("No experience found")

    if exp_id!="new":
        user_experience=Experience.objects.filter(user_id=current_user_id,id=int(exp_id))
        if user_experience:
            user_exp_data=user_experience[0]
            user_experience_form=ExperienceForm(instance=user_exp_data)
            print(user_experience_form)
        else:
            raise Http404("No experience found")
    
    return render(request,"experience.html",{'user_experience_form':user_experience_form})



@login_required
def showEditableProfile(request):
    current_user_id=request.user.id

    if request.method=="POST":
        print(request.POST,request.FILES)
        profile=UserExtraDetails.objects.get(user_id=current_user_id)

        form = UserExtraDetailsForm(request.POST,request.FILES,instance=profile)
        user_form=UserForm(data=request.POST,instance=request.user)
        print(user_form.fields.keys())


        if form.is_valid():
            
            obj=form.save()
            if 'user_resume' not in request.FILES:
                print("user_r not changed",profile.user_resume)
                obj.user_resume=profile.user_resume
            if 'user_image' not in request.FILES:
                print("user_image not changed",profile.user_image)
                obj.user_image=profile.user_image
            obj.save()
            form.initial['user_resume']=obj.user_resume
            # print (obj.user_resume,obj.user_image)

        if user_form.is_valid() and user_form.changed_data:
            if 'username' in user_form.changed_data and User.objects.filter(username=user_form.cleaned_data['username']).exists():
                messages.info(request,"Username taken")
                return redirect('profile')
            elif 'email' in  user_form.changed_data and User.objects.filter(email=user_form.cleaned_data['email']).exists():
                messages.info(request,"Email exists")
                return redirect('profile')
            else:
                print("valid user from")
                user_form.save()
        
        
        messages.info(request,"Information Updated")


    print('GET')
    current_user_id=request.user.id
    # print(type(current_user_id))
    user_extra_details=UserExtraDetails.objects.get(user_id=current_user_id)
    user_info=User.objects.get(id=current_user_id)

    # print(user_extra_details,type(user_info))
    user_details_form=UserExtraDetailsForm(initial={'user_interest':user_extra_details.user_interest,'user_address':user_extra_details.user_address,'user_project_completed':user_extra_details.user_project_completed,'user_image':user_extra_details.user_image,'user_resume':user_extra_details.user_resume})
    print(user_details_form)
    user_info_form=UserForm(initial={'first_name':user_info.first_name,'last_name':user_info.last_name,'username':user_info.username,'email':user_info.email})
    return render(request,"profile.html",{'user_details_form':user_details_form,'user_info_form':user_info_form})