from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .models import UserExtraDetails
# Create your views here.

def viewprofile(request,user_id):
    print(request,"viewprofile")
    return render(request,"profile.html",{'user_id':user_id})


@login_required
def showEditableProfile(request):
    current_user_id=request.user.id

    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print("valid Form")
            profile_id=UserExtraDetails.objects.get(user_id=current_user_id)
            form.save(request.user,profile_id.id)
            
            # form.user.add(*[request.user])
        print(form)
        # user_ins=user_extra_details.cleaned_data['user_intrest']
        # print (form.)
        return render(request,"profile.html",{'user_details_form':form})


    print('ffffffff')
    current_user_id=request.user.id
    print(type(current_user_id))
    user_extra_details=UserExtraDetails.objects.get(user_id=current_user_id)

    print(user_extra_details)
    user_details_form=UserForm(initial={'user_interest':user_extra_details.user_interest,'user_address':user_extra_details.user_address,'user_project_completed':user_extra_details.user_project_completed})
    
    return render(request,"profile.html",{'user_details_form':user_details_form})