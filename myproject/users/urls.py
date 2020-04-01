from django.urls import path,re_path

from . import views

urlpatterns = [
    path("profile/<str:username>",views.viewProfile,name="viewprofile"),
    path("profile/",views.showEditableProfile,name="profile"),
    # path("experience/",views.showExperience,name="experience"),
    # path("experience/<str:exp_id>",views.editableExperience,name="editexperience"),
    # path("experience/<str:exp_id>/delete/",views.deleteExperience,name="deleteexperience"),
    # path("education/",views.showEducation,name="education"),
    # path("education/<str:education_id>",views.editableEducation,name="editeducation"),
    # path("education/<str:education_id>/delete/",views.deleteEducation,name="deleteeducation"),
    # path("award/",views.showAward,name="award"),
    # path("award/<str:award_id>",views.editableAward,name="editaward"),
    # path("award/<str:award_id>/delete/",views.deleteAward,name="deleteaward"),
    path("user/<str:category>/",views.showCategory,name="category"),
    path("user/<str:category>/<str:category_id>",views.editableCategory,name="editablecategory"),
    path("user/<str:category>/<str:category_id>/delete/",views.deleteCategory,name="deletecategory"),
    path("profile/<str:username>/projects/",views.userProjects,name="userprojects"),
    path("sendemail/<str:username>",views.sendemail,name="sendemail"),
    path("",views.index,name="index"),
    path("projects",views.projects,name="projects"),







]