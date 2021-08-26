from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import grade_inputForm
from .models import grades
from Career_Passport.mixins import StudentMixin,TeacherMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class grade_input(LoginRequiredMixin,StudentMixin,generic.FormView):
    template_name='grade_management/grade_register.html'
    model=grades
    form_class=grade_inputForm
    success_url='grade_management:grade_input'