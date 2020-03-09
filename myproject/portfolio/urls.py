from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),

    path("getprojectinfo/<int:pk>",views.getprojectinfo,name="getprojectinfo")
]