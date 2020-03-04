from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name='Mumbai'
    dest1.desc='The City That Never Sleeps'
    dest1.price = 700
    dest1.img = 'destination_2.jpg'
    dest1.offer = False


    return render(request,"travello_index.html",{'dests':[dest1]})