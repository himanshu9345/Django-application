from django.urls import path,re_path

from . import views

urlpatterns = [
    path("<str:user_id>",views.viewprofile,name="profile"),
    path("",views.showEditableProfile,name="profile")
]