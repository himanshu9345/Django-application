from django.shortcuts import render,redirect
from .forms import UserExtraDetailsForm,UserForm,ExperienceForm
from django.contrib.auth.decorators import login_required
from .models import UserExtraDetails,Experience
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def viewprofile(request,user_id):
    print(request,"viewprofile")
    return render(request,"index.html",{'user_id':user_id})

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
def EditableExperience(request,exp_id):
    current_user_id=request.user.id
    user_experience_form=ExperienceForm()
    user_exp_data=None
    if request.method=='POST':
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

    if exp_id!="new":
        user_experience=Experience.objects.filter(user_id=current_user_id,id=int(exp_id))
        if user_experience:
            user_exp_data=user_experience[0]
            user_experience_form=ExperienceForm(instance=user_exp_data)
            print(user_experience_form)
    
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