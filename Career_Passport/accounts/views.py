from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LoginView(LoginRequiredMixin,generic.TemplateView):
    template_name='registration/index.html'
    def get(self,request,**kwargs):
        category=str(self.request.user.category_type.all()[0])
        if category=="生徒":
            return redirect('/looking_back/student_confirm')
        elif category=="先生":
            return redirect('/teacher_confirmation/teacher_confirm')
        else :
            return redirect('/admin')