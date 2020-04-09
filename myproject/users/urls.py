from django.urls import path,re_path

from . import views

urlpatterns = [
    path("profile/<str:username>",views.viewProfile,name="viewprofile"),
    path("profile/",views.showEditableProfile,name="profile"),
    path("user/<str:category>/",views.showCategory,name="category"),
    path("user/<str:category>/<str:category_id>",views.editableCategory,name="editablecategory"),
    path("user/<str:category>/<str:category_id>/delete/",views.deleteCategory,name="deletecategory"),
    path("profile/<str:username>/projects/",views.userProjects,name="userprojects"),
    path("sendemail/<str:username>",views.sendemail,name="sendemail"),
    path("",views.index,name="index"),
    path("projects",views.projects,name="projects"),

]