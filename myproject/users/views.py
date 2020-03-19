from django.shortcuts import render

# Create your views here.

def viewprofile(request,user_id):
    print(request)
    return render(request,"profile.html",{'user_id':user_id})


def showEditableProfile(request):
    print(request)
    return render(request,"profile.html")