from django.shortcuts import render,redirect
from .models import Experience,Skill,Award,Publication,Project
from django.core.mail import send_mail
from django.conf import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from django.contrib import messages


# Create your views here.
def index(request):
    exps = Experience.objects.all().order_by('-end_year')
    skills = Skill.objects.all().order_by('-percentage_you_know')
    awards = Award.objects.all().order_by('-award_year')
    publications = Publication.objects.all().order_by('-publication_date')
    projects = Project.objects.all().order_by('-project_end_year')
    print(awards)
    return render(request,"index.html",{'exps':exps,'skills':skills,'awards':awards,'publications':publications,'projects':projects})

def projects(request):
    app_url = "/"
    projects = Project.objects.all().order_by('-project_end_year')

    print(app_url,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render(request,"projects.html",{'app_url': app_url,'projects':projects})

def loadsection(request):
    return render(request,"index.html")
        
def sendemail(request):
    if request.method=="POST":
        person_name=request.POST['person_name']
        email=request.POST['email']
        email_subject=request.POST['email_subject']
        message=request.POST['message']
        # print(message,email,person_name,email_subject)

        to_sender="Hello "+person_name+",\n"+"you will be contacted soon. <br>"+"Your Message was, <strong>"+message+"<strong>"
        to_sender_subject="Replay from Himanshu"
        # #requester
        # # send_mail(to_sender_subject,to_sender,settings.EMAIL_HOST_USER1,[settings.EMAIL_HOST_USER1],fail_silently=False,)
        
        # #myself
        to_me="Hello Himanshu,\n"+"you got contacted by "+person_name+" <br>"+"Message for you is, <strong>"+message+"<strong>"

        

        message1 = Mail(
            from_email='faltu9345@gmail.com',
            to_emails='hbp53@njit.edu',
            subject=email_subject,
            html_content=to_me)
        message2 = Mail(
            from_email='faltu9345@gmail.com',
            to_emails=email,
            subject=to_sender_subject,
            html_content=to_sender)
        try:
            
            sg = SendGridAPIClient(os.getenv('SEND_GRID_KEY'))
            response = sg.send(message1)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            response = sg.send(message2)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
            print("nope")

        return render(request,'index.html')
    else:
        
        return render(request,'index.html')
