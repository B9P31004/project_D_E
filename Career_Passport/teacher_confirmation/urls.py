"""Career_Passport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='teacher_confirmation'

urlpatterns = [
    #path('',views.IndexView.as_view(),name="index"),
    path('teacher_confirm',views.Index.as_view(),name="index"),
    path('student_list/<int:pk>',views.student_list.as_view(),name="student_list"),
    path('career_passport_confirm/<int:pk>/<int:id>',views.career_passport_confirm.as_view(),name="career_passport_confirm"),
    path('career_passport_confirm_output/<int:pk>/<int:id>',views.career_passport_confirm_output.as_view(),name="career_passport_confirm_output"),
    path('grade_output_confirm/<int:pk>/<int:id>',views.grade_output_confirm.as_view(),name="grade_output_confirm"),
]
