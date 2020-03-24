from django.urls import path,re_path

from . import views

urlpatterns = [
    path("profile/<str:user_id>",views.viewprofile,name="profile"),
    path("profile/",views.showEditableProfile,name="profile"),
    path("experiences/",views.showExperience,name="experiences"),
    path("experiences/<str:exp_id>",views.editableExperience,name="editexperience"),
    path("experiences/<str:exp_id>/delete/",views.deleteExperience,name="deleteexperience"),
    path("educations/",views.showEducation,name="educations"),
    path("educations/<str:education_id>",views.editableEducation,name="editeducation"),
    path("educations/<str:education_id>/delete/",views.deleteEducation,name="deleteeducation"),
    path("awards/",views.showAward,name="awards"),
    path("awards/<str:award_id>",views.editableAward,name="editaward"),
    path("awards/<str:award_id>/delete/",views.deleteAward,name="deleteaward"),

]