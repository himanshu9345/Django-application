from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from users.models import UserExtraDetails
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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                userdetails = UserExtraDetails(user_id=user.id)
                user.save()
                userdetails.save()
                print("user created")
                return redirect('login')

        else:
            messages.info(request,"Password dont match")
            return redirect('register')


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