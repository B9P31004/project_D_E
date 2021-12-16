from django.shortcuts import render
from django.views import generic
from .forms import FileUploadForm
from .models import FileSave
from accounts.models import School
from django.contrib.auth.mixins import LoginRequiredMixin
from Career_Passport.mixins import TeacherMixin,StudentMixin
from django.http import HttpResponse
import json

# Create your views here.
class FileUploadView(LoginRequiredMixin,TeacherMixin,generic.CreateView):
    template_name="file_uploader/file_upload.html"
    form_class=FileUploadForm

    def post(self,request,*args,**kwargs):
        if FileSave.objects.filter(title=request.POST['title'],semester=request.POST['semester']):
            file=FileSave.objects.get(title=request.POST['title'],semester=request.POST['semester'])
        else:    
            file=FileSave()
        file.title=request.POST['title']
        file.school=School.objects.get(id=self.request.user.school_ID.id)
        file.semester=request.POST['semester']
        file.event_name=request.POST['event_name']
        file.file=request.FILES['file']
        file.save()
        print(request.POST)

        next_form=FileUploadForm
        context={
            'message':'成功しました',
            'form':next_form
        }
        return render(request,'file_uploader/file_upload.html',context)

class event_output(LoginRequiredMixin,StudentMixin,generic.DetailView):
    def get(self,request,**kwargs):
        semester=int(request.GET.get('semester'))
        def get_object(semester):
            data_store=[]
            if FileSave.objects.filter(semester=semester):
                event_object=[]
                for i in range(1,4):
                    if FileSave.objects.filter(event_name=i,semester=semester):
                        pre_event_object=FileSave.objects.filter(event_name=i,semester=semester)
                        for item in pre_event_object:
                            event_object.append(item.file.url)
                        data_store.append(event_object)
                    else:
                        data_store.append('データがありません')
                return data_store
            else:
                return 'データがありません'
        event=get_object(semester)
        if type(event)!=str:
            response={
                'event_1':event[0],
                'event_2':event[1],
                'event_3':event[2],
                'empty':1
            }
            response_json=json.dumps(response)
        else:
            response={
                'empty':event
            }
            response_json=json.dumps(response)
        return HttpResponse(response_json)