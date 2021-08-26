from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LoginView(LoginRequiredMixin,generic.TemplateView):
    template_name='looking_back/index.html'
