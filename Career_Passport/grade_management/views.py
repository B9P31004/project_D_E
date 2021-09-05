from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import grade_inputForm
from .models import grades
from Career_Passport.mixins import StudentMixin,TeacherMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json

# Create your views here.

class grade_input(LoginRequiredMixin,StudentMixin,generic.FormView):
    template_name='grade_management/grade_register.html'
    model=grades
    form_class=grade_inputForm
    def get_success_url(self):
        return redirect('grade_management:grade_register_confirm', pk=self.kwargs['pk'])
    
    def post(self,request,*args,**kwargs):
        if 'button_input' in request.POST:
            context={
                'grade_lists':[
                    request.POST.get('school_year'),
                    request.POST.get('semester'),
                    request.POST.get('regular_test'),
                    request.POST.get('national_language'),
                    request.POST.get('math'),
                    request.POST.get('english'),
                    request.POST.get('social_studies'),
                    request.POST.get('science'),
                    request.POST.get('music'),
                    request.POST.get('art'),
                    request.POST.get('technical_arts_and_home_economics'),
                    request.POST.get('health_and_physical_education')
                ]
            }
            request.session['form_data']=request.POST
            return render(request,'grade_management/grade_register_confirm.html',context)
        elif 'button_confirm' in request.POST:
            form=request.session.get('form_data')
            school_year=form['school_year']
            semester=form['semester']
            regular_test=form['regular_test']
            if grades.objects.filter(UniqueID=self.request.user,school_year=school_year,semester=semester,regular_test=regular_test).exists():
                context={
                    'comment':'データが既にあります。更新ページから更新してください'
                }
                return render(request,'looking_back/career_passport_result.html',context)
            else:
                form=request.session.get('form_data')
                form=grade_inputForm(form)
                if form.is_valid():
                    form=form.save(commit=False)
                    form.UniqueID=self.request.user
                    print(form)
                    form.save()
                context={
                    'comment':'成功しました'
                }
                return render(request,'looking_back/career_passport_result.html',context)
        elif 'button_confirm_back' in request.POST:
            form=grade_inputForm(request.session.get('form_data'))
            context={
                'form':form,
            }
            return render(request,'grade_management/grade_register.html',context)

class grade_output(LoginRequiredMixin,StudentMixin,generic.DetailView):
    def post(self,request,*args,**kwargs):
        select=int(request.POST.get('select'))
        def get_object(select):
            if(select==10101):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=1,regular_test="中間")
                return grade_object
            elif(select==10102):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=1,regular_test="期末")
                return grade_object
            elif(select==10201):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=2,regular_test="中間")
                return grade_object
            elif(select==10202):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=2,regular_test="期末")
                return grade_object
            elif(select==10301):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=3,regular_test="中間")
                return grade_object
            elif(select==10302):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=3,regular_test="期末")
                return grade_object
            elif(select==20101):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=1,regular_test="中間")
                return grade_object
            elif(select==20102):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=1,regular_test="期末")
                return grade_object
            elif(select==20201):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=2,regular_test="中間")
                return grade_object
            elif(select==20202):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=2,regular_test="期末")
                return grade_object
            elif(select==20301):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=3,regular_test="中間")
                return grade_object
            elif(select==20302):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=2,semester=3,regular_test="期末")
                return grade_object
            elif(select==30101):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=1,regular_test="中間")
                return grade_object
            elif(select==30102):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=1,regular_test="期末")
                return grade_object
            elif(select==30201):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=2,regular_test="中間")
                return grade_object
            elif(select==30202):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=2,regular_test="期末")
                return grade_object
            elif(select==30301):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=3,regular_test="中間")
                return grade_object
            elif(select==30302):
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=3,semester=3,regular_test="期末")
                return grade_object

            """else:
                grade_object=grades.objects.get(UniqueID=self.request.user.id,school_year=1,semester=1)
                return grade_object"""
        grade=get_object(select)
        response={
            'national_language':grade.national_language,
            'math':grade.math,
            'english':grade.english,
            'social_studies':grade.social_studies,
            'science':grade.science,
            'music':grade.music,
            'art':grade.art,
            'technical_arts_and_home_economics':grade.technical_arts_and_home_economics,
            'health_and_physical_education':grade.health_and_physical_education,
        }
        response_json=json.dumps(response)
        return HttpResponse(response_json)