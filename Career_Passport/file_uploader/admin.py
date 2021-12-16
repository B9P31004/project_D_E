from django.contrib import admin
from .models import FileSave

# Register your models here.
class FileSaveAdmin(admin.ModelAdmin):
    list_display=['title','school','semester','event_name','file']
    list_filter=['title','school','semester','event_name','file']

admin.site.register(FileSave,FileSaveAdmin)