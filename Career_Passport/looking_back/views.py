from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Career_Passport.mixins import StudentMixin,StudentIndexMixin
from itertools import chain
from file_uploader.models import FileSave
import json
import os
from django.http import HttpResponse
from looking_back.modules import rw_career_passport_json as rw_json
from looking_back.modules import semester_confirm
from looking_back.modules import np_analize
from looking_back.modules import rw_occupational_aptitude

#from datetime import datetime
#from pytz import timezone

# Create your views here.

class IndexView(LoginRequiredMixin,StudentIndexMixin,generic.TemplateView):
    template_name='looking_back/index.html'
    def get(self,request,**kwargs):
        semester=semester_confirm.semester_confirm()
        context={
            'semester':semester,
        }
        return render(request,'looking_back/index.html',context)

class occupational_aptitude(LoginRequiredMixin,StudentMixin,generic.TemplateView):
    template_name='looking_back/occupational_attitude'
    def get(self,request,**kwargs):
        data=rw_occupational_aptitude.occupatonal_aptitude_original_read()
        context={}
        context["question"]=data
        context["length"]=len(data)
        return render(request,'looking_back/occupational_aptitude.html',context)

    def post(self,request,*args,**kwargs):
        data=rw_occupational_aptitude.occupatonal_aptitude_original_read()
        if 'button_input' in request.POST:
            loop=int(request.POST.get('length'))
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(request.POST.get(str(i)))
            context={}
            context['question']=data
            context['result']=r_list
            request.session['form_data']=request.POST
            return render(request,'looking_back/occupational_aptitude_confirm.html',context)
        elif 'button_confirm' in request.POST:
            f_data=request.session.get('form_data')
            r_data=[]
            a_data=[]
            for i in range(0,int(f_data["length"]),1):
                r_data.append(f_data[str(i)])
            rw_occupational_aptitude.occupational_aptitude_write(self.request.user.school_ID.id,self.request.user.user_ID,r_data)
            for text in r_data:
                a_data.append(np_analize.judge_np(text))
            sf_comment=np_analize.occupational_aptitude(self.request.user.school_ID.id,self.request.user.user_ID)
            context={
                'comment':sf_comment,
                'result_url':1
            }
            return render(request,'looking_back/occupational_aptitude_input_result.html',context)
        elif 'button_confirm_back' in request.POST:
            f_data=request.session.get('form_data')
            loop=int(f_data['length'])
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(f_data[str(i)])
            context={}
            context['question']=data
            context['result']=r_list
            context["length"]=len(data)
            return render(request,'looking_back/occupational_aptitude.html',context)

class occupational_aptitude_result(LoginRequiredMixin,StudentMixin,generic.TemplateView):
    template_name='occupational_aptitude_result.html'
    def get(self,request,**kwargs):
        question=rw_occupational_aptitude.occupatonal_aptitude_original_read()
        data=rw_occupational_aptitude.occupational_aptitude_read(self.request.user.school_ID.id,self.request.user.user_ID)
        if type(data)!=str:
            result=data['result']
            analize=data['analize']
            qra=[question,result,analize]
            context={
                'question':question,
                'result':result,
                'analize':analize
            }
        else:
            context={
                'empty':data
            }
        return render(request,'looking_back/occupational_aptitude_result.html',context)

class occupational_aptitude_output(LoginRequiredMixin,StudentMixin,generic.DetailView):
    def get(self,request,*args,**kwargs):
        def get_object():
            occupational_aptitude_object=rw_occupational_aptitude.occupational_aptitude_read(self.request.user.school_ID.id,self.request.user.user_ID)
            return occupational_aptitude_object
        occupational_aptitude=get_object()
        if type(occupational_aptitude)!=str:
            question=rw_occupational_aptitude.occupatonal_aptitude_original_read()
            response={
                'question':question,
                'result':occupational_aptitude['result'],
                'analize':occupational_aptitude['analize'],
                'empty':1
            }
            response_json=json.dumps(response)
        else:
            response={
                'empty':occupational_aptitude
            }
            response_json=json.dumps(response)
        return HttpResponse(response_json)


class career_passport_edit_s(LoginRequiredMixin,StudentMixin,generic.TemplateView):
    template_name="looking_back/career_passport_edit.html"
    def get(self,request,**kwargs):
        semester=semester_confirm.semester_confirm()
        data=rw_json.career_passport_original_read(self.request.user.school_ID.id,self.request.user.student_year,semester,'s')
        context={
            'year':self.request.user.student_year,
            'semester':semester,
        }
        if os.path.isfile('static/career_passport/'+str(self.request.user.school_ID.id)+'/student_register/career_passport_'+str(self.request.user.user_ID)+'.json')==True:
            s_data=rw_json.get_career_passport(self.request.user.school_ID.id,self.request.user.user_ID)
            if 'student_career_passport_'+str(self.request.user.student_year) in s_data:
                if 'semester_'+str(semester) in s_data['student_career_passport_'+str(self.request.user.student_year)]:
                    if 'result_s' in s_data['student_career_passport_'+str(self.request.user.student_year)]['semester_'+str(semester)]["result"][0]:
                        context["result"]=s_data['student_career_passport_'+str(self.request.user.student_year)]['semester_'+str(semester)]["result"][0]["result_s"]
                        if len(data)>len(context["result"]):
                            context["result"].append("")
        context["question"]=data
        context["length"]=len(data)
        return render(request,'looking_back/career_passport_edit.html',context)

    def post(self,request,*args,**kwargs):
        semester=semester_confirm.semester_confirm()
        data=rw_json.career_passport_original_read(self.request.user.school_ID.id,self.request.user.student_year,semester,'s')
        if 'button_input' in request.POST:
            loop=int(request.POST.get('length'))
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(request.POST.get(str(i)))
            context={
                'year':self.request.user.student_year,
                'semester':semester,
            }
            context['question']=data
            context['result']=r_list
            request.session['form_data']=request.POST
            return render(request,'looking_back/career_passport_confirm.html',context)
        elif 'button_confirm' in request.POST:
            f_data=request.session.get('form_data')
            r_data=[]
            a_data=[]
            for i in range(0,int(f_data["length"]),1):
                r_data.append(f_data[str(i)])
            rw_json.career_passport_edit(self.request.user.school_ID.id,self.request.user.student_year,semester,self.request.user.user_ID,r_data,'s')
            for text in r_data:
                a_data.append(np_analize.judge_np(text))
            sf_comment=np_analize.register(self.request.user.school_ID.id,self.request.user.student_year,semester,self.request.user.user_ID,a_data,'s')
            context={
                'comment':sf_comment
            }
            return render(request,'looking_back/career_passport_result.html',context)
        elif 'button_confirm_back' in request.POST:
            f_data=request.session.get('form_data')
            loop=int(f_data['length'])
            context={
                'year':self.request.user.student_year,
                'semester':semester,
            }
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(f_data[str(i)])
            context['question']=data
            context['result']=r_list
            context["length"]=len(data)
            return render(request,'looking_back/career_passport_edit.html',context)

class career_passport_edit_e(LoginRequiredMixin,StudentMixin,generic.TemplateView):
    template_name="looking_back/career_passport_edit.html"
    def get(self,request,**kwargs):
        semester=semester_confirm.semester_confirm()
        data=rw_json.career_passport_original_read(self.request.user.school_ID.id,self.request.user.student_year,semester,'e')
        context={
            'year':self.request.user.student_year,
            'semester':semester,
        }
        if os.path.isfile('static/career_passport/'+str(self.request.user.school_ID.id)+'/student_register/career_passport_'+str(self.request.user.user_ID)+'.json')==True:
            s_data=rw_json.get_career_passport(self.request.user.school_ID.id,self.request.user.user_ID)
            if 'student_career_passport_'+str(self.request.user.student_year) in s_data:
                if 'semester_'+str(semester) in s_data['student_career_passport_'+str(self.request.user.student_year)]:
                    if 'result_s' in s_data['student_career_passport_'+str(self.request.user.student_year)]['semester_'+str(semester)]["result"][0]:
                        context["result"]=s_data['student_career_passport_'+str(self.request.user.student_year)]['semester_'+str(semester)]["result"][0]["result_e"]
                        if len(data)>len(context["result"]):
                            context["result"].append("")
        context["question"]=data
        context["length"]=len(data)
        return render(request,'looking_back/career_passport_edit.html',context)

    def post(self,request,*args,**kwargs):
        semester=semester_confirm.semester_confirm()
        data=rw_json.career_passport_original_read(self.request.user.school_ID.id,self.request.user.student_year,semester,'e')
        if 'button_input' in request.POST:
            loop=int(request.POST.get('length'))
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(request.POST.get(str(i)))
            context={
                'year':self.request.user.student_year,
                'semester':semester,
            }
            context['question']=data
            context['result']=r_list
            request.session['form_data']=request.POST
            return render(request,'looking_back/career_passport_confirm.html',context)
        elif 'button_confirm' in request.POST:
            f_data=request.session.get('form_data')
            r_data=[]
            a_data=[]
            for i in range(0,int(f_data["length"]),1):
                r_data.append(f_data[str(i)])
            rw_json.career_passport_edit(self.request.user.school_ID.id,self.request.user.student_year,semester,self.request.user.user_ID,r_data,'e')
            for text in r_data:
                a_data.append(np_analize.judge_np(text))
            sf_comment=np_analize.register(self.request.user.school_ID.id,self.request.user.student_year,semester,self.request.user.user_ID,a_data,'e')
            context={
                'comment':sf_comment,
            }
            return render(request,'looking_back/career_passport_result.html',context)
        elif 'button_confirm_back' in request.POST:
            f_data=request.session.get('form_data')
            loop=int(f_data['length'])
            context={
                'year':self.request.user.student_year,
                'semester':semester,
            }
            r_list=[]
            for i in range(0,loop,1):
                r_list.append(f_data[str(i)])
            context['question']=data
            context['result']=r_list
            context["length"]=len(data)
            return render(request,'looking_back/career_passport_edit.html',context)

class career_passport_detail(LoginRequiredMixin,StudentMixin,generic.DetailView):
    template_name='looking_back/career_passport_detail.html'
    
    def get(self, request, **kwargs):
        option_c={}
        for y in range(1,4):
            if y ==self.request.user.student_year:
                option_c[y*10]='<option selected value="'+str(y)+'0''">'+str(y)+'年</option>'
            else:
                option_c[y*10]='<option value="'+str(y)+'0''">'+str(y)+'年</option>'

        context={
            'career_passport_option_list':[
                option_c,
            ]
        }
        return render(request,'looking_back/career_passport_detail.html',context)

class career_passport_output(LoginRequiredMixin,StudentMixin,generic.DetailView):
    def post(self,request,*args,**kwargs):
        select=request.POST.get('select')
        def get_object(select):
            if(select=='101s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,1,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='101e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,1,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='102s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,2,self.request.user.user_ID)
                print(career_passport_object)
                return career_passport_object,'s'
            elif(select=='102e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,2,self.request.user.user_ID)
                print(career_passport_object)
                return career_passport_object,'e'
            elif(select=='103s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,3,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='103e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,1,3,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='201s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,1,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='201e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,1,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='202s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,2,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='202e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,2,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='203s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,3,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='203e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,2,3,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='301s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,1,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='301e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,1,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='302s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,2,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='302e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,2,self.request.user.user_ID)
                return career_passport_object,'e'
            elif(select=='303s'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,3,self.request.user.user_ID)
                return career_passport_object,'s'
            elif(select=='303e'):
                career_passport_object=rw_json.select_career_passport(self.request.user.school_ID.id,3,3,self.request.user.user_ID)
                return career_passport_object,'e'
        career_passport=get_object(select)
        if type(career_passport[0])!=str:
            if 'question_'+career_passport[1] in career_passport[0]['question'][0]:
                response={
                    'question':career_passport[0]['question'][0]['question_'+career_passport[1]],
                    'result':career_passport[0]['result'][0]['result_'+career_passport[1]],
                    'empty':1
                }
                if 'comment' in career_passport[0]:
                    if 'comment_'+career_passport[1] in career_passport[0]['comment'][0]:
                        add_comment_view={
                            'comment':career_passport[0]['comment'][0]['comment_'+career_passport[1]]
                        }
                        response.update(add_comment_view)
                response_json=json.dumps(response)
            else:
                response={
                    'empty':career_passport[0]
                }
                response_json=json.dumps(response)
        else:
            response={
                'empty':career_passport[0]
            }
            response_json=json.dumps(response)
        return HttpResponse(response_json)

class book(LoginRequiredMixin,StudentIndexMixin,generic.TemplateView):
    template_name='looking_back/book.html'
    def get(self, request, **kwargs):
        book_reserch=self.kwargs.get('book')
        data=rw_json.read_book_data(book_reserch)
        if data!=0:
            context={
                'length':len(data['title']),
                'title':data['title'],
                'author':data['author'],
                'publisher':data['publisher'],
                'year':data['year'],
                'category':data['category'],
                'etc':data['etc'],
                'book':book_reserch
            }
        else:
            context={
                'length':data
            }
        print(data)
        return render(request,'looking_back/book.html',context)

class EventView(LoginRequiredMixin,StudentIndexMixin,generic.TemplateView):
    template_name='looking_back/event.html'

class load(generic.TemplateView):
    template_name='looking_back/load.html'