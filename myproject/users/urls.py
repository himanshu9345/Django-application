from django.urls import path,re_path

from . import views

urlpatterns = [
    path("profile/<str:user_id>",views.viewprofile,name="profile"),
    path("profile/",views.showEditableProfile,name="profile"),
    path("experiences/",views.showExperience,name="experiences"),
    path("experiences/<str:exp_id>",views.EditableExperience,name="editexperience"),
    path("experiences/<str:exp_id>/delete/",views.deleteExperience,name="deleteexperience"),


]