from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm,UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser,Role,School,CategoryType

# Register your models here.
class CustomUserAdmin(UserAdmin,admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    """def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category_type":
            kwargs["queryset"] = CategoryType.objects.order_by('category_type')
        return super().formfield_for_manytomany(db_field, request, **kwargs)"""
    
    fieldsets=(
        (None,{'fields':('user_ID','password')}),
        ('personal info',{'fields':('school_ID','student_year','student_class')}),
        ('permissions',{'fields':('is_active','is_admin','user_permissions','role','category_type')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_ID','name','school_ID','student_year','student_class','password1', 'password2'),
        }),
    )
    list_display=['user_ID','name','school_ID','student_year','is_active','is_admin']#'school_name','school_ID','school_year','class_ID','school_share_ID','parents_share_ID']
    list_filter=('is_active','is_admin','school_ID','student_year','student_class','category_type')
    search_fields=('user_ID',)
    ordering = ('user_ID',)
    filter_horizontal = ('user_permissions','role','category_type')

class SchoolAdmin(admin.ModelAdmin):
    list_display=['school_name']
    list_filter=['school_name']

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display=['type_name']

class RoleAdmin(admin.ModelAdmin):
    list_display=['role']

"""class StudentAdmin(admin.ModelAdmin):
    list_display=['student_ID','school_ID','student_class','student_year']
    list_filter=['school_ID','student_class','student_year']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['teacher_ID','school_ID','homeroom_class','class_year']
    list_filter=['school_ID','homeroom_class','class_year']

class ParentsAdmin(admin.ModelAdmin):
    list_display=['parents_ID','child_ID']"""

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(School,SchoolAdmin)
admin.site.register(CategoryType,CategoryTypeAdmin)
admin.site.register(Role,RoleAdmin)
"""admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Parents,ParentsAdmin)"""