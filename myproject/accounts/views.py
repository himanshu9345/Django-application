from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from users.models import UserExtraDetails,ContactDetails
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from .models import UserToken

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists")
                return render(request,"register.html")

            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                userdetails = UserExtraDetails(user_id=user.id)
                user.save()
                userdetails.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request,"Password dont match")
            return render(request,"register.html")


    else:
        return render(request,"register.html")


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("usrr foun3")
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            return redirect('profile')
        else:
            messages.info(request,"Invalid Credentials")
            print("usrr not foun2")
            return redirect('login')
    else:
        print("usrr not foun1")

        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')


def passwordResetEmail(request):
    if request.method=="POST":
        user=None
        try:
            email=request.POST['email']
            user= get_object_or_404(User, email=email)
            unique_id = get_random_string(length=20)
            user_token_object = UserToken.objects.get(user_id=user.id)

            if not user_token_object:
                user_token_object=UserToken(user=user,access_token=unique_id)
                user_token_object.save()
            else:
                user_token_object.access_token=unique_id
                user_token_object.save(update_fields=["access_token"]) 
        except Exception as e:
            print(e)
            messages.info(request,"Email not found")

    return render(request,'password-reset.html',{'beforeReset':True})

def passwordResetEmailSent(request):
    message="We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly."
    return render(request,'password-reset-done.html',{'message':message})


def passwordReset(request):
    return render(request,'password-reset.html')


def passwordResetDone(request):
    message=" Your password has been set. You may go ahead and sign in"
    return render(request,'password-reset-done.html',{'message':message})