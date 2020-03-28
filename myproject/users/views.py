from django.shortcuts import render,redirect
from .forms import UserExtraDetailsForm,UserForm,ExperienceForm,EducationForm,AwardForm,SkillForm,PublicationForm,ProjectForm,ContactDetailsForm
from django.contrib.auth.decorators import login_required
from .models import UserExtraDetails,Experience,Education,Award,Skill,Publication,Project,ContactDetails
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import os
load_dotenv()
# Create your views here.
category_name_model_form_dict={'skill':[Skill,SkillForm,'Skill','skill',SkillForm()],\
    'publication':[Publication,PublicationForm,'Publication','publication',PublicationForm()],\
    'project':[Project,ProjectForm,'Project','project',ProjectForm()],\
    'education':[Education,EducationForm,'Education',"education",EducationForm()], 
    'experience':[Experience,ExperienceForm,'Experience','experience',ExperienceForm()], 
    'contactdetails':[ContactDetails,ContactDetailsForm,'ContactDetails','contactdetails',ContactDetailsForm()], 
    
    'award':[Award,AwardForm,'Award','award',AwardForm()]}

def index(request):
    username=os.getenv('MY_ID')
    user=None
    isAdmin=True
    try:
        user= get_object_or_404(User, username=username)
    except:
        raise Http404("User not found")
    exps = Experience.objects.all().filter(user_id=user.id).order_by('-end_month_year')
    skills = Skill.objects.all().filter(user_id=user.id).order_by('-percentage_you_know')
    awards = Award.objects.all().filter(user_id=user.id).order_by('-award_month_year')
    publications = Publication.objects.all().filter(user_id=user.id).order_by('-publication_date')
    projects = Project.objects.all().filter(user_id=user.id).order_by('-project_end_month_year')
    education = Education.objects.all().filter(user_id=user.id).order_by('-college_end_month_year')
    contactdetails = ContactDetails.objects.all().filter(user_id=user.id)
    user_details=User.objects.get(id=user.id)
    user_extra_details=UserExtraDetails.objects.get(user_id=user.id)
    return render(request,"userprofile.html",{'isAdmin':isAdmin,'exps':exps,'skills':skills,'awards':awards,'publications':publications,'projects':projects,'username':username,'user_details':user_details,'user_extra_details':user_extra_details,'education':education,'contactdetails':contactdetails})

def projects(request):
    app_url = "/"
    username=os.getenv('MY_ID')
    user= get_object_or_404(User, username=username)
    projects = Project.objects.all().filter(user_id=user.id).order_by('-project_end_month_year')
    print(app_url,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",projects)
    return render(request,"projects.html",{'app_url': app_url,'projects':projects})



def viewProfile(request,username):
    isAdmin=False
    print("in view Profile",username)
    user=None
    try:
        user= get_object_or_404(User, username=username)
    except:
        raise Http404("User not found")
    exps = Experience.objects.all().filter(user_id=user.id).order_by('-end_month_year')
    skills = Skill.objects.all().filter(user_id=user.id).order_by('-percentage_you_know')
    awards = Award.objects.all().filter(user_id=user.id).order_by('-award_month_year')
    publications = Publication.objects.all().filter(user_id=user.id).order_by('-publication_date')
    projects = Project.objects.all().filter(user_id=user.id).order_by('-project_end_month_year')
    education = Education.objects.all().filter(user_id=user.id).order_by('-college_end_month_year')
    contactdetails = ContactDetails.objects.all().filter(user_id=user.id)
    user_details=User.objects.get(id=user.id)
    user_extra_details=UserExtraDetails.objects.get(user_id=user.id)
    return render(request,"userprofile.html",{'isAdmin':isAdmin,'exps':exps,'skills':skills,'awards':awards,'publications':publications,'projects':projects,'username':username,'user_details':user_details,'user_extra_details':user_extra_details,'education':education,'contactdetails':contactdetails})
    
def userProjects(request,username):
    user=None
    user_url="/".join(request.build_absolute_uri().split("/projects/")[:-1])
    try:
        user= get_object_or_404(User, username=username)
    except:
        raise Http404("User not found")
    projects = Project.objects.all().filter(user_id=user.id).order_by('-project_end_month_year')
    
    # print(app_url,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render(request,"projects.html",{'app_url': user_url,'projects':projects})

def convertToCamelCase(word):
    return ' '.join(x.capitalize() or '_' for x in word.split('_'))

@login_required
def editableCategory(request,category,category_id):
    if category in category_name_model_form_dict:
        to_edit=False
        current_user_id=request.user.id
        user_category_form=category_name_model_form_dict[category][4]
        user_category_data=None
        if request.method=='POST':
            user_category=None
            if category_id!='new':
                user_category=category_name_model_form_dict[category][0].objects.filter(user_id=current_user_id,id=int(category_id))
            if user_category:
                user_category_data=user_category[0]
            
            if user_category or category_id=='new':
                user_category_form=category_name_model_form_dict[category][1](request.POST,request.FILES,instance=user_category_data)

                if user_category_form.is_valid:
                    print(user_category_form)
                    
                    obj=user_category_form.save(commit=False)
                    if category_id=='new':
                        obj.user_id=current_user_id
                    obj.save()
                    return HttpResponseRedirect(reverse('category',args=(category_name_model_form_dict[category][3],)))
                else:
                    print(user_category_form.errors)

            else:
                raise Http404("No "+category_name_model_form_dict[category][2]+" found")
                
        else:
            if category_id!="new":
                to_edit=True
                user_category=category_name_model_form_dict[category][0].objects.filter(user_id=current_user_id,id=int(category_id))
                if user_category:
                    user_category_data=user_category[0]
                    user_category_form=category_name_model_form_dict[category][1](instance=user_category_data)
                    print(user_category_form)
                else:
                    raise Http404("No "+category_name_model_form_dict[category][2]+" found")

    
        return render(request,"commoneditableform.html",{'form_requested':user_category_form,'type_of_user_detail':category_name_model_form_dict[category][3],'model_name':category_name_model_form_dict[category][2],'isEdit':to_edit})



@login_required
def showCategory(request,category):
    print("inshow category",category)
    if category in category_name_model_form_dict:
        current_user_id=request.user.id
        user_awards=category_name_model_form_dict[category][0].objects.filter(user_id=current_user_id)
        print(user_awards)
        fieldlist=[convertToCamelCase(f.name)  for f in category_name_model_form_dict[category][0]._meta.get_fields() if f.name!='user']
        return render(request,"commondisplaypage.html",{'fieldlist':fieldlist,'user_forms':user_awards,'type_of_user_detail':category_name_model_form_dict[category][3],'model_name':category_name_model_form_dict[category][2]})
    else:
        raise Http404("Page not found")

@login_required
def deleteCategory(request,category,category_id):
    try:
        user_category= get_object_or_404(category_name_model_form_dict[category][0], pk=category_id)
        user_category.delete()
        return HttpResponseRedirect(reverse('category',args=(category_name_model_form_dict[category][3],)))
    except:
        raise Http404("No "+category_name_model_form_dict[category][2]+" found")

def sendemail(request,username):#remaining
    user=None
    if request.method=="POST":
        try:
            user= get_object_or_404(User, username=username)
        except:
            raise Http404("User not found")
        person_name=request.POST['person_name']
        email=request.POST['email']
        email_subject=request.POST['email_subject']
        message=request.POST['message']
        to_sender="Hello "+person_name+",\n"+"you will be contacted soon. <br>"+"Your Message was, <strong>"+message+"<strong>"
        to_sender_subject="Replay from "+user.first_name
        to_user="Hello "+user.first_name+",\n"+" <br>you got contacted by "+person_name+" <br>"+"Message for you is, <strong>"+message+"</strong></br>"+" <br> sender emailid - "+email+"</br>"
        message1 = Mail(
            from_email='faltu9345@gmail.com',
            to_emails=user.email,
            subject=email_subject,
            html_content=to_user)
        message2 = Mail(
            from_email='faltu9345@gmail.com',
            to_emails=email,
            subject=to_sender_subject,
            html_content=to_sender)
        try:
            
            sg = SendGridAPIClient(os.getenv('SEND_GRID_KEY'))
            response = sg.send(message1)
            print(response.status_code)
            print(response.body)
            print(response.headers)
            response = sg.send(message2)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
            print("nope")

        return redirect('viewprofile',username=username)

    else:
        
        return redirect('viewprofile',username=username)


# @login_required
# def showAward(request):
#     current_user_id=request.user.id
#     user_awards=Award.objects.filter(user_id=current_user_id)
#     fieldlist=[convertToCamelCase(f.name)  for f in Award._meta.get_fields() if f.name!='user']
#     return render(request,"commondisplaypage.html",{'fieldlist':fieldlist,'user_forms':user_awards,'type_of_user_detail':'award','model_name':'Award'})

# @login_required
# def deleteAward(request,award_id):
#     try:
#         user_award= get_object_or_404(award, pk=award_id)
#         user_award.delete()
#         return redirect('award')

#     except:
#         raise Http404("No award found")


# @login_required
# def editableAward(request,award_id):
#     to_edit=False
#     current_user_id=request.user.id
#     user_award_form=AwardForm()
#     user_award_data=None
#     if request.method=='POST':
#         user_award=None
#         if award_id!='new':
#             user_award=Award.objects.filter(user_id=current_user_id,id=int(award_id))
#         if user_award:
#             user_award_data=user_award[0]
        
#         if user_award or award_id=='new':
#             user_award_form=AwardForm(data=request.POST,instance=user_award_data)
#             obj=user_award_form.save(commit=False)
            
#             if award_id=='new':
#                 obj.user_id=current_user_id
#             obj.save()
#             return redirect('award')
#         else:
#             raise Http404("No education found")
            
#     else:
#         if award_id!="new":
#             to_edit=True
#             user_award=Award.objects.filter(user_id=current_user_id,id=int(award_id))
#             if user_award:
#                 user_award_data=user_award[0]
#                 user_award_form=AwardForm(instance=user_award_data)
#                 print(user_award_form)
#             else:
#                 raise Http404("No award found")
    
#     return render(request,"commoneditableform.html",{'form_requested':user_award_form,'type_of_user_detail':'award','model_name':'Award','isEdit':to_edit})



# @login_required
# def showEducation(request):
#     current_user_id=request.user.id
#     user_educations=Education.objects.filter(user_id=current_user_id)
#     return render(request,"educations.html",{'user_educations':user_educations})

# @login_required
# def deleteEducation(request,education_id):
#     try:
#         user_education= get_object_or_404(Education, pk=exp_id)
#         user_education.delete()
#         return redirect('education')

#     except:
#         raise Http404("No education found")


# @login_required
# def editableEducation(request,education_id):
#     current_user_id=request.user.id
#     user_education_form=EducationForm()
#     user_education_data=None
#     if request.method=='POST':
#         user_education=None
#         if education_id!='new':
#             user_education=Education.objects.filter(user_id=current_user_id,id=int(education_id))
#         if user_education:
#             user_education_data=user_education[0]
        
#         if user_education or education_id=='new':
#             user_education_form=EducationForm(data=request.POST,instance=user_education_data)
#             obj=user_education_form.save(commit=False)
            
#             if education_id=='new':
#                 obj.user_id=current_user_id
#             obj.save()
#             return redirect('education')
#         else:
#             raise Http404("No Education found")
            
#     else:
#         if education_id!="new":
#             user_education=Education.objects.filter(user_id=current_user_id,id=int(education_id))
#             if user_education:
#                 user_education_data=user_education[0]
#                 user_education_form=EducationForm(instance=user_education_data)
#                 print(user_education_form)
#             else:
#                 raise Http404("No education found")
    
#     return render(request,"education.html",{'user_education_form':user_education_form})


# @login_required
# def showExperience(request):
#     current_user_id=request.user.id
#     user_experiences=Experience.objects.filter(user_id=current_user_id)

#     # print (exp_id)
#     return render(request,"experiences.html",{'user_experiences':user_experiences})

# @login_required
# def deleteExperience(request,exp_id):
#     try:
#         user_experience= get_object_or_404(Experience, pk=exp_id)
#         user_experience.delete()
#         return redirect('experience')

#     except:
#         raise Http404("No experience found")


# @login_required
# def editableExperience(request,exp_id):
#     current_user_id=request.user.id
#     user_experience_form=ExperienceForm()
#     user_exp_data=None
#     if request.method=='POST':
#         try:
#             user_experience=None
#             if exp_id!='new':
#                 user_experience=Experience.objects.filter(user_id=current_user_id,id=int(exp_id))
#             if user_experience:
#                 user_exp_data=user_experience[0]
                
#             user_experience_form=ExperienceForm(data=request.POST,instance=user_exp_data)
#             obj=user_experience_form.save(commit=False)
            
#             if exp_id=='new':
#                 obj.user_id=current_user_id
#             obj.save()
#             return redirect('experience')
#         except:
#             raise Http404("No experience found")

#     if exp_id!="new":
#         user_experience=Experience.objects.filter(user_id=current_user_id,id=int(exp_id))
#         if user_experience:
#             user_exp_data=user_experience[0]
#             user_experience_form=ExperienceForm(instance=user_exp_data)
#             print(user_experience_form)
#         else:
#             raise Http404("No experience found")
    
#     return render(request,"experience.html",{'user_experience_form':user_experience_form})



@login_required
def showEditableProfile(request):
    current_user_id=request.user.id

    if request.method=="POST":
        print(request.POST,request.FILES)
        profile=UserExtraDetails.objects.get(user_id=current_user_id)

        form = UserExtraDetailsForm(request.POST,request.FILES,instance=profile)
        user_form=UserForm(data=request.POST,instance=request.user)
        print(user_form.fields.keys())


        if form.is_valid():
            
            obj=form.save()
            if 'user_resume' not in request.FILES:
                print("user_r not changed",profile.user_resume)
                obj.user_resume=profile.user_resume
            if 'user_image' not in request.FILES:
                print("user_image not changed",profile.user_image)
                obj.user_image=profile.user_image
            obj.save()
            form.initial['user_resume']=obj.user_resume
            # print (obj.user_resume,obj.user_image)

        if user_form.is_valid() and user_form.changed_data:
            if 'username' in user_form.changed_data and User.objects.filter(username=user_form.cleaned_data['username']).exists():
                messages.info(request,"Username taken")
                return redirect('profile')
            elif 'email' in  user_form.changed_data and User.objects.filter(email=user_form.cleaned_data['email']).exists():
                messages.info(request,"Email exists")
                return redirect('profile')
            else:
                print("valid user from")
                user_form.save()
        
        
        messages.info(request,"Information Updated")


    print('GET')
    current_user_id=request.user.id
    # print(type(current_user_id))
    user_extra_details=UserExtraDetails.objects.get(user_id=current_user_id)
    user_info=User.objects.get(id=current_user_id)

    # print(user_extra_details,type(user_info))
    user_details_form=UserExtraDetailsForm(initial={'user_interest':user_extra_details.user_interest,'user_address':user_extra_details.user_address,'user_project_completed':user_extra_details.user_project_completed,'user_image':user_extra_details.user_image,'user_resume':user_extra_details.user_resume})
    print(user_details_form)
    user_info_form=UserForm(initial={'first_name':user_info.first_name,'last_name':user_info.last_name,'username':user_info.username,'email':user_info.email})
    return render(request,"profile.html",{'user_details_form':user_details_form,'user_info_form':user_info_form})