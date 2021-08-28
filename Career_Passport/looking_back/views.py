from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import TextForm,career_passport01_1_Form
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Career_Passport.mixins import StudentMixin
from itertools import chain
from .models import career_passport01_1
from grade_management.models import grades

#from datetime import datetime
#from pytz import timezone

# Create your views here.

class IndexView(LoginRequiredMixin,generic.TemplateView):
    template_name='looking_back/index.html'

class analizeView(generic.FormView):
    template_name='looking_back/analize.html'
    form_class=TextForm
    success_url=reverse_lazy('looking_back:analyze')
    def post(self,request,*args,**kwargs):
        text=request.POST.get('text')
        return render(request,self.template_name,{'text':text})
    #return text

class career_passport01_1_input(LoginRequiredMixin,StudentMixin,generic.FormView):
    model=career_passport01_1
    template_name="looking_back/career_passport_input.html"
    form_class=career_passport01_1_Form
    #success_url=reverse_lazy('looking_back:career_passport01_1_confirm')
    def get_success_url(self):
        return redirect('looking_back:career_passport01_1_confirm', pk=self.kwargs['pk'])
    #def get_success_url(self):
        #return redirect(reverse_lazy('looking_back:career_passport01_1_confirm',kwargs={'pk':self.kwargs['pk']}))
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['pk'] = self.kwargs['pk']        
        #return context
    #def form_valid(self,form):
    #            query_set=form.save(commit=False)
    #            query_set.user_id=self.request.user
    #            print(query_set)
    #            query_set.save()
    #            return super().form_valid(form)

    def post(self,request,*args,**kwargs):
        if 'button_input' in request.POST:
            #print (request.POST)
            context={
                'career_passport_lists':[
                    request.POST.get('my_current'),
                    request.POST.get('my_PR'),
                    request.POST.get('my_dream'),
                    request.POST.get('getting_skills'),
                    request.POST.get('study_target'),
                    request.POST.get('for_study_target'),
                    request.POST.get('life_target'),
                    request.POST.get('for_life_target'),
                    request.POST.get('local_target'),
                    request.POST.get('for_local_target'),
                    request.POST.get('others_target'),
                    request.POST.get('for_others_target')
                ]
            }
            request.session['form_data']=request.POST
            return render(request,'looking_back/career_passport_confirm.html',context)
        elif 'button_confirm' in request.POST:
            if career_passport01_1.objects.filter(UniqueID=self.request.user).exists():
                context={
                    'comment':'データが既にあります。更新ページから更新してください'
                }
                return render(request,'looking_back/career_passport_result.html',context)
            else:
                form=request.session.get('form_data')
                form=career_passport01_1_Form(form)
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
            form=career_passport01_1_Form(request.session.get('form_data'))
            context={
                'form':form,
            }
            return render(request,'looking_back/career_passport_input.html',context)


#class career_passport01_1_confirm(generic.FormView):
#    success_url=reverse_lazy('looking_back:index')
#    def get(self,request,*args,**kwargs):
#        context={
#            "my_current":"a",
#        }
#        return render(request,self.template_name,context)

class career_passport01_1_detail(LoginRequiredMixin,StudentMixin,generic.DetailView):
    #model=career_passport01_1
    template_name='looking_back/career_passport_detail.html'
    #slug_field='UniqueID'
    #slug_url_kwarg='UniqueID'
    #pk_url_kwarg='UniqueID'

    #def get_queryset(self):
    #    queryset=career_passport01_1.objects.filter(UniqueID=self.request.user).all()
    #    print(self.request.user.id)
    #    print(queryset)
    #    return queryset

    """def get_context_data(self,**kwargs):
        context=get_context_data(UniqueID=self.request.user.id)
        context.update({
            'grades':grades.objects.get(UniqueID=self.request.user.id)
        })
        return context"""

    """def get_queryset(self):
        x=career_passport01_1.objects.filter(UniqueID=self.request.user).values()
        y=grades.objects.filter(UniqueID=self.request.user.id)
        print(type(x))
        print(x)
        return x
        #career_passport01_1.objects.get(UniqueID=self.request.user.id)"""

    #model=grades
    def get_object(self,queryset=None):
        #if grades.objects.filter(UniqueID=self.request.user).exists():
            #return grades.objects.get(UniqueID=self.request.user.id)
        return career_passport01_1.objects.get(UniqueID=self.request.user.id)

class career_passport01_1_edit(generic.UpdateView):
    template_name='looking_back/career_passport_edit.html'
    model=career_passport01_1
    form_class=career_passport01_1_Form
    def get_success_url(self):
        return redirect('looking_back:career_passport01_1_confirm', pk=self.kwargs['pk'])
    def get_form(self):
        form = super(career_passport01_1_edit, self).get_form()
        return form
    def get_object(self,queryset=None):
        if career_passport01_1.objects.filter(UniqueID=self.request.user).exists():
            return career_passport01_1.objects.get(UniqueID=self.request.user.id)
        else:
            context={
                'comment':'データが登録されていません'
            }
    
    def post(self,request,*args,**kwargs):
        if 'button_edit' in request.POST:
            #print (request.POST)
            context={
                'career_passport_lists':[
                    request.POST.get('my_current'),
                    request.POST.get('my_PR'),
                    request.POST.get('my_dream'),
                    request.POST.get('getting_skills'),
                    request.POST.get('study_target'),
                    request.POST.get('for_study_target'),
                    request.POST.get('life_target'),
                    request.POST.get('for_life_target'),
                    request.POST.get('local_target'),
                    request.POST.get('for_local_target'),
                    request.POST.get('others_target'),
                    request.POST.get('for_others_target')
                ]
            }
            request.session['form_data']=request.POST
            return render(request,'looking_back/career_passport_confirm.html',context)
        elif 'button_confirm' in request.POST:
            cache=request.session.get('form_data')
            cp_document=career_passport01_1.objects.get(UniqueID=self.request.user.id)
            cp_document.my_current=cache['my_current']
            cp_document.my_PR=cache['my_PR']
            cp_document.my_dream=cache['my_dream']
            cp_document.getting_skills=cache['getting_skills']
            cp_document.study_target=cache['study_target']
            cp_document.for_study_target=cache['for_study_target']
            cp_document.life_target=cache['life_target']
            cp_document.for_life_target=cache['for_life_target']
            cp_document.local_target=cache['local_target']
            cp_document.for_local_target=cache['for_local_target']
            cp_document.others_target=cache['others_target']
            cp_document.for_others_target=cache['for_others_target']
            cp_document.save()
            #career_passport01_1.objects.bulk_update(cp_document,fields=['my_current','my_PR','my_dream','getting_skills','study_target','for_study_target','life_target','for_life_target','local_target','for_local_target','others_target','others_target','for_others_target'])
            """form=request.session.get('form_data')
            form=career_passport01_1_Form(form)
            if form.is_valid():
                    form=form.save(commit=False)
                    form.UniqueID=self.request.user
                    print(form.my_dream)
                    form.save()
            def form_valid(self,form):
                messages.success(self.request,'更新しました')
                return super().form_valid(form)
            def form_valid(self,form):
                messages.error(self.request,'更新できませんでした')
                return super().form_valid(form)"""
            context={
                'comment':'成功しました'
            }
            return render(request,'looking_back/career_passport_result.html',context)
        elif 'button_confirm_back' in request.POST:
            form=career_passport01_1_Form(request.session.get('form_data'))
            a=request.session.get('form_data')
            print(a['my_dream'])
            context={
                'form':form,
            }
            return render(request,'looking_back/career_passport_edit.html',context)