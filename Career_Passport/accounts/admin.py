from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,School,Student,Teacher,Parents

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    fieldsets=UserAdmin.fieldsets#+((None,{'fields':('school_name','school_ID','school_year','class_ID','school_share_ID','parents_share_ID')}),)
    list_display=['username','email']#'school_name','school_ID','school_year','class_ID','school_share_ID','parents_share_ID']

class SchoolAdmin(admin.ModelAdmin):
    list_display=['school_name']
    list_filter=['school_name']

class StudentAdmin(admin.ModelAdmin):
    list_display=['student_ID','school_ID','student_class','student_year']
    list_filter=['school_ID','student_class','student_year']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_ID','school_ID','homeroom_class','class_year']
    list_filter=['school_ID','homeroom_class','class_year']

class ParentsAdmin(admin.ModelAdmin):
    list_display=['parents_ID','child_ID']

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Parents,ParentsAdmin)