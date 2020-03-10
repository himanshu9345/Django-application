from django.urls import path,re_path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index.html",views.index),
    path("projects",views.projects,name="projects")
]