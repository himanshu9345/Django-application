from django.shortcuts import render
from .models import Experience,Skill,Award,Publication,Project
# from django.core.mail import send_mail

# Create your views here.
def index(request):
    exps = Experience.objects.all()
    skills = Skill.objects.all()
    awards = Award.objects.all()
    publications = Publication.objects.all()
    projects = Project.objects.all()
    print(awards)
    return render(request,"index.html",{'exps':exps,'skills':skills,'awards':awards,'publications':publications,'projects':projects})

def getprojectinfo(request,pk):
    if request.method=="GET":
        project=Project.objects.get(id=pk)
        return render(request,"projects.html",{'project':project})
# def sendemail(request):
#     if request.method=='POST':rtr
        
