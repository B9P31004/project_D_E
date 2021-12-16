from django.shortcuts import render,redirect
from django.views import generic
from django.http import HttpResponse
import os
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from Career_Passport.mixins import TeacherMixin,TeacherIndexMixin
from accounts.models import CustomUser
from looking_back.modules import rw_career_passport_json as rw_json
from grade_management.models import grades
from accounts.models import CategoryType
# Create your views here.

class Index(LoginRequiredMixin,TeacherIndexMixin,generic.TemplateView):
    template_name='teacher_confirmation/index.html'

class student_list(LoginRequiredMixin,TeacherMixin,generic.ListView):
    template_name="teacher_confirmation/student_list.html"
    def get(self,request,**kwargs):
        category_type=CategoryType.objects.get(type_name='生徒')
        query_set=CustomUser.objects.filter(school_ID=self.request.user.school_ID.id,student_year=self.request.user.student_year,student_class=self.request.user.student_class,category_type=category_type.id)
        context={
            "student_list":query_set,
        }
        return render(request,'teacher_confirmation/student_list.html',context)

class career_passport_confirm(LoginRequiredMixin,TeacherMixin,generic.DetailView):
    template_name='teacher_confirmation/career_passport_confirmation.html'

    def get(self, request, **kwargs):
        student_id=self.kwargs.get('id')
        student_data=CustomUser.objects.get(user_ID=student_id)
        option_c={}
        for y in range(1,4):
            if y ==self.request.user.student_year:
                option_c[y*10]='<option selected value="'+str(y)+'0''">'+str(y)+'年</option>'
            else:
                option_c[y*10]='<option value="'+str(y)+'0''">'+str(y)+'年</option>'

        context={
            'year':student_data.student_year,
            'class':student_data.student_class,
            'name':student_data.name,
            'teacher_year':self.request.user.student_year,
            'career_passport_option_list':[
                option_c,
            ],
            'id':student_id,
        }
        return render(request,'teacher_confirmation/career_passport_confirmation.html',context)
    
    def post(self,request,*args,**kwargs):
        student_id=self.kwargs.get('id')
        option_c={}
        data=rw_json.get_career_passport(self.request.user.school_ID.id,student_id)
        for y in range(1,4):
            if y ==self.request.user.student_year:
                option_c[y*10]='<option selected value="'+str(y)+'0''">'+str(y)+'年</option>'
            else:
                option_c[y*10]='<option value="'+str(y)+'0''">'+str(y)+'年</option>'

        #data=rw_json.career_passport_original_read(self.request.user.school_ID.id,self.request.user.student_year,semester)
        if 'button_input' in request.POST:
            student_data=CustomUser.objects.get(user_ID=student_id)
            split_ys=list(request.POST.get('select_text'))
            se_text=''
            if int(split_ys[3])==0:
                se_text='初め'
            elif int(split_ys[3])==1:
                se_text='終り'
            context={
                'year':student_data.student_year,
                'class':student_data.student_class,
                'name':student_data.name,
                'select_year':split_ys[0],
                'select_semester':split_ys[2],
                'select_se':se_text,
                'comment':request.POST.get('confirm_comment'),
            }
            request.session['form_data']=request.POST
            return render(request,'teacher_confirmation/confirm.html',context)
        elif 'button_confirm' in request.POST:
            student_data=CustomUser.objects.get(user_ID=student_id)
            f_data=request.session.get('form_data')
            comment=f_data['confirm_comment']
            select_pre_number=f_data["select_text"]
            select_number=list(select_pre_number)
            if int(select_number[3])==0:
                sf_comment=rw_json.career_passport_add_comment(self.request.user.school_ID.id,select_number[0],select_number[2],student_id,comment,'s')
            elif int(select_number[3])==1:
                sf_comment=rw_json.career_passport_add_comment(self.request.user.school_ID.id,select_number[0],select_number[2],student_id,comment,'e')
            context={
                'year':student_data.student_year,
                'class':student_data.student_class,
                'name':student_data.name,
                'comment':sf_comment,
                'id':student_id,
            }
            return render(request,'teacher_confirmation/career_passport_result.html',context)
        elif 'button_confirm_back' in request.POST:
            student_data=CustomUser.objects.get(user_ID=student_id)
            f_data=request.session.get('form_data')
            print(f_data)
            context={
                'year':student_data.student_year,
                'class':student_data.student_class,
                'name':student_data.name,
                'comment':f_data['confirm_comment'],
                'teacher_year':self.request.user.student_year,
                'select':f_data['select_text'],
                'career_passport_option_list':[
                    option_c,
                ],
                'id':student_id,
            }
            return render(request,'teacher_confirmation/career_passport_confirmation.html',context)

class career_passport_confirm_output(LoginRequiredMixin,TeacherMixin,generic.DetailView):
    def post(self,request,*args,**kwargs):
        student_id=self.kwargs.get('id')
        select=int(request.POST.get('select'))
        def get_object(select):
            if(select==1010 or select==1011):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,1,student_id)
                return career_passport_object
            elif(select==1020 or select==1021):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,2,student_id)
                return career_passport_object
            elif(select==1030 or select==1031):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,3,student_id)
                return career_passport_object
            elif(select==2010 or select==2011):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,1,student_id)
                return career_passport_object
            elif(select==2020 or select==2021):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,2,student_id)
                return career_passport_object
            elif(select==2030 or select==2031):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,3,student_id)
                return career_passport_object
            elif(select==3010 or select==3011):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,1,student_id)
                return career_passport_object
            elif(select==3020 or select==3021):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,2,student_id)
                return career_passport_object
            elif(select==3030 or select==3031):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,3,student_id)
                return career_passport_object
        career_passport=get_object(select)
        if career_passport=='データがありません':
            response={
                'empty':'データがありません'
            }
        else:
            if select%10==0:
                response={
                    'question':career_passport['question'][0]['question_s'],
                    'result':career_passport['result'][0]['result_s'],
                    'empty':1
                }
            elif select%10==1:
                response={
                    'question':career_passport['question'][0]['question_e'],
                    'result':career_passport['result'][0]['result_e'],
                    'empty':1
                }
            if 'comment' in career_passport:
                if 'comment_s' in career_passport['comment'][0] and select%10==0:
                    add_comment_view={
                        'comment':career_passport['comment'][0]['comment_s']
                    }
                    response.update(add_comment_view)
                if 'comment_e' in career_passport['comment'][0] and select%10==1:
                    add_comment_view={
                        'comment':career_passport['comment'][0]['comment_e']
                    }
                    response.update(add_comment_view)
            if 'analize' in career_passport:
                if 'analize_s' in career_passport['analize'][0] and select%10==0:
                    add_analize_view={
                        'analize':career_passport['analize'][0]['analize_s']
                    }
                    response.update(add_analize_view)
                if 'analize_e' in career_passport['analize'][0] and select%10==1:
                    add_analize_view={
                        'analize':career_passport['analize'][0]['analize_e']
                    }
                    response.update(add_analize_view)
        response_json=json.dumps(response)
        return HttpResponse(response_json)

class grade_output_confirm(LoginRequiredMixin,TeacherMixin,generic.DetailView):
    def post(self,request,*args,**kwargs):
        student_id=self.kwargs.get('id')
        select=int(request.POST.get('select'))
        def get_object(select):
            if(select==10101):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=1,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=1,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==10102):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=1,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=1,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==10201):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=2,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=2,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==10202):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=2,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=2,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==10301):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=3,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=3,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==10302):
                if grades.objects.filter(UniqueID=student_id,school_year=1,semester=3,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=1,semester=3,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==20101):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=1,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=1,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==20102):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=1,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=1,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==20201):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=2,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=2,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==20202):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=2,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=2,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==20301):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=3,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=3,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==20302):
                if grades.objects.filter(UniqueID=student_id,school_year=2,semester=3,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=2,semester=3,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==30101):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=1,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=1,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==30102):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=1,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=1,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==30201):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=2,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=2,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==30202):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=2,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=2,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            elif(select==30301):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=3,regular_test="中間").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=3,regular_test="中間")
                else:
                    grade_object=None
                return grade_object
            elif(select==30302):
                if grades.objects.filter(UniqueID=student_id,school_year=3,semester=3,regular_test="期末").exists():
                    grade_object=grades.objects.get(UniqueID=student_id,school_year=3,semester=3,regular_test="期末")
                else:
                    grade_object=None
                return grade_object
            #else:
            #    None
        grade=get_object(select)
        if grade==None:
            response={
                'grade_error_flag':'該当するデータはありません'
            }
            response_json=json.dumps(response)
        else:
            response={
                'grade_error_flag':1,
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
