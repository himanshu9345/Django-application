from django.contrib import admin
from .models import Experience,Skill,Award,Publication,Project
# Register your models here.


class ExperienceAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Experience._meta.fields]

class SkillAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Skill._meta.fields]

class AwardAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Award._meta.fields]

class PublicationAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Publication._meta.fields]

class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Project._meta.fields]

admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Award,AwardAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Project,ProjectAdmin)