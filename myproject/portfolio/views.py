from django.shortcuts import render,redirect
from .models import Experience,Skill,Award,Publication,Project
from django.core.mail import send_mail
from django.conf import settings

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
        print(message,email,person_name,email_subject)

        to_sender="Hello "+person_name+",\n"+"you will be contacted soon\n"+"Your Message was, "+message
        to_sender_subject="Replay from Himanshu"
        #requester
        send_mail(to_sender_subject,to_sender,settings.EMAIL_HOST_USER1,[settings.EMAIL_HOST_USER1],fail_silently=False,)
        
        #myself
        to_me="Hello Himanshu,\n"+"you got contacted by "+person_name+" \n"+"Message for you is, "+message
        # send_mail(email_subject,to_me,settings.EMAIL_HOST_USER1,['hbp53@njit.edu'],fail_silently=False,)
        return redirect('index')
    else:
        return redirect('index')

