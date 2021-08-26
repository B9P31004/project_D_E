from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import TextForm,career_passport01_1_inputForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from Career_Passport.mixins import StudentMixin
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
    form_class=career_passport01_1_inputForm
    success_url=reverse_lazy('looking_back:career_passport01_1_confirm')
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
                print('error')
            else:
                form=request.session.get('form_data')
                form=career_passport01_1_inputForm(form)
                if form.is_valid():
                    form=form.save(commit=False)
                    form.UniqueID=self.request.user
                    print(form)
                    form.save()
            return redirect('looking_back:index')
        elif 'button_confirm_back' in request.POST:
            form=career_passport01_1_inputForm(request.session.get('form_data'))
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
    model=career_passport01_1
    template_name='looking_back/detail.html'
    #slug_field='UniqueID'
    #slug_url_kwarg='UniqueID'
    #pk_url_kwarg='UniqueID'

    #def get_queryset(self):
    #    queryset=career_passport01_1.objects.filter(UniqueID=self.request.user).all()
    #    print(self.request.user.id)
    #    print(queryset)
    #    return queryset
    def get_object(self,queryset=None):
        return career_passport01_1.objects.get(UniqueID=self.request.user.id)

    model=grades
    def get_object(self,queryset=None):
        if career_passport01_1.objects.filter(UniqueID=self.request.user).exists():
            return grades.objects.get(UniqueID=self.request.user.id)