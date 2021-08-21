from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    fieldsets=UserAdmin.fieldsets+((None,{'fields':('school_name','school_ID','school_year','class_ID')}),)
    list_display=['username','email','school_name','school_ID','school_year','class_ID']

admin.site.register(CustomUser,CustomUserAdmin)