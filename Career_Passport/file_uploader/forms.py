from django import forms
from .models import FileSave

class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FileSave
        fields=('title','semester','event_name','file')