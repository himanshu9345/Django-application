from django.shortcuts import render
from .models import Experience,Skill,Award,Publication

# Create your views here.
def index(request):
    exps = Experience.objects.all()
    skills = Skill.objects.all()
    awards = Award.objects.all()
    publications = Publication.objects.all()
    print(awards)
    return render(request,"index.html",{'exps':exps,'skills':skills,'awards':awards,'publications':publications})