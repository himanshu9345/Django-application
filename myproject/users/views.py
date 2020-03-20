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
    print('ffffffff')
    current_user_id=request.user.id
    print(type(current_user_id))
    user_extra_details=UserExtraDetails.objects.get(user_id=current_user_id)

    print(user_extra_details)
    user_details_form=UserForm()
    
    return render(request,"profile.html",{'user_details_form':user_details_form})
    return render(request,"profile.html")