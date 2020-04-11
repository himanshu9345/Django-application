from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from users.models import UserExtraDetails,ContactDetails
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import UserToken
import os
from dotenv import load_dotenv
load_dotenv()

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

        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def sendMailSendGrid(to_emails,subject,html_content):
    # message1 = Mail(
    #         from_email='faltu9345@gmail.com',
    #         to_emails=user.email,
    #         subject=email_subject,
    #         html_content=to_user)
    message = Mail(
        from_email='faltu9345@gmail.com',
        to_emails=to_emails,
        subject=subject,
        html_content=html_content)
    try:
        sg = SendGridAPIClient(os.getenv('SEND_GRID_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return True
    except Exception as e:
        return False


def passwordResetEmail(request):
    if request.method=="POST":
        user=None
        try:
            email=request.POST['email']
            user= get_object_or_404(User, email=email)
            unique_id = get_random_string(length=20)
            user_token_object=None
            try:
                user_token_object = UserToken.objects.get(user_id=user.id)
            except:
                print("New reset request")

            if not user_token_object:
                user_token_object=UserToken(user=user,access_token=unique_id)
                user_token_object.save()
            else:
                user_token_object.access_token=unique_id
                user_token_object.save(update_fields=["access_token"])
                auth_url='http://'+os.getenv('IP')+"/accounts/reset/"+ unique_id
                print(auth_url)
                to_email=email
                subject="Password Recovery"
                html_content="This e-mail is in response to your recent request to recover a forgotten password <br/> <br/> <a target='_blank' href="+auth_url+">Click here to reset your password</a> <br/> If you are having trouble accessing the link, copy and paste the following link address into your browser window: </br></br>"+auth_url
                if not sendMailSendGrid(to_email,subject,html_content):
                    message="Please try again later, Email service not working"
                    return render(request,'password-reset-done.html',{'message':message})
                
        except Exception as e:
            print(e)
            print("Error in passwordResetEmail")
        message="We've emailed you instructions for setting your password, if an account exists with the email("+email+") you entered. You should receive them shortly."
        return render(request,'password-reset-done.html',{'message':message})


    return render(request,'password-reset.html',{'beforeReset':True})

def passwordResetEmailSent(request):
    message="We've emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly."
    return render(request,'password-reset-done.html',{'message':message})


def passwordReset(request,token):
    if request.method=='POST':
        user_token_object=None
        try:
            user_token_object = get_object_or_404(UserToken,access_token=token)
            user=User.objects.get(id=user_token_object.user_id)
            if request.POST['password1']!=request.POST['password2']:
                messages.info(request,"Password don't match")
                return render(request,'password-reset.html',{'beforeReset':False})
            else:
                user.set_password(request.POST['password1'])
                user.save()
                return redirect('password_reset_done')

        except Exception as e:
            message="Link Expired"
            return render(request,'password-reset-done.html',{'message':message})

    return render(request,'password-reset.html',{'beforeReset':False})


def passwordResetDone(request):
    message=" Your password has been set. You may go ahead and login in"
    return render(request,'password-reset-done.html',{'message':message})