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

app_name='looking_back'

urlpatterns = [
    path('student_confirm',views.IndexView.as_view(),name="index"),
    path('career_passport_edit_s/<int:pk>',views.career_passport_edit_s.as_view(),name="career_passport_edit_s"),
    path('career_passport_edit_e/<int:pk>',views.career_passport_edit_e.as_view(),name="career_passport_edit_e"),
    path('career_passport_detail/<int:pk>',views.career_passport_detail.as_view(),name="career_passport_detail"),
    path('career_passport_output/<int:pk>',views.career_passport_output.as_view(),name="career_passport_output"),
    path('occupational_aptitude/<int:pk>',views.occupational_aptitude.as_view(),name="occupational_aptitude"),
    path('occupational_aptitude_result/<int:pk>',views.occupational_aptitude_result.as_view(),name="occupational_aptitude_result"),
    path('occupational_aptitude_output/<int:pk>',views.occupational_aptitude_output.as_view(),name="occupational_aptitude_output"),
    path('book/<int:pk>/<str:book>',views.book.as_view(),name="book"),
    path('event/<int:pk>',views.EventView.as_view(),name="event"),
    path('load/',views.load.as_view(),name="load"),
]