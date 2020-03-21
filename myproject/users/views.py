from django.shortcuts import render,redirect
from .forms import UserExtraDetailsForm,UserForm
from django.contrib.auth.decorators import login_required
from .models import UserExtraDetails
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def viewprofile(request,user_id):
    print(request,"viewprofile")
    return render(request,"profile.html",{'user_id':user_id})


@login_required
def showEditableProfile(request):
    current_user_id=request.user.id

    if request.method=="POST":
        form = UserExtraDetailsForm(request.POST)
        user_form=UserForm(data=request.POST,instance=request.user)
        print(user_form.fields.keys())

        if form.is_valid():
            profile_id=UserExtraDetails.objects.get(user_id=current_user_id)
            form.save(request.user,profile_id.id)
        if user_form.is_valid():
            if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                messages.info(request,"Username taken")
                return redirect('profile')
            elif User.objects.filter(email=user_form.cleaned_data['email']).exists():
                messages.info(request,"Email exists")
                return redirect('profile')
            else:
                print("valid user from")
                user_form.save()
        return render(request,"profile.html",{'user_details_form':form})


    print('ffffffff')
    current_user_id=request.user.id
    print(type(current_user_id))
    user_extra_details=UserExtraDetails.objects.get(user_id=current_user_id)
    user_info=User.objects.get(id=current_user_id)

    print(user_extra_details,type(user_info))
    user_details_form=UserExtraDetailsForm(initial={'user_interest':user_extra_details.user_interest,'user_address':user_extra_details.user_address,'user_project_completed':user_extra_details.user_project_completed})
    user_info_form=UserForm(initial={'first_name':user_info.first_name,'last_name':user_info.last_name,'username':user_info.username,'email':user_info.email})
    return render(request,"profile.html",{'user_details_form':user_details_form,'user_info_form':user_info_form})