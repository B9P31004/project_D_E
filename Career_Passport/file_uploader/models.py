from os import name
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import School

# Create your models here.
TITLE_CHOICES = (('title_1','タイトル1'),('title_2','タイトル2'),('title_3','タイトル3'),('title_4','タイトル4'),('title_5','タイトル5'),('title_6','タイトル6'),('title_7','タイトル7'),('title_8','タイトル8'))
EVENT_CHOICES = ((1,'イベント1'),(2,'イベント2'),(3,'イベント3'))
SEMESTER_CHOICES=((1,'1学期'),(2,'2学期'),(3,'3学期'))
def save_select_path(instance,filename):
    ext=filename.split('.')[-1]
    new_name=instance.title
    return '{0}/{1}/{2}/{3}/{4}.{5}'.format('event',instance.school_id,instance.semester,instance.event_name,new_name,ext)

class FileSave(models.Model):
    title=models.CharField(choices=TITLE_CHOICES,max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    semester=models.IntegerField(choices=SEMESTER_CHOICES,validators=[MinValueValidator(1), MaxValueValidator(3)])
    event_name=models.IntegerField(choices=EVENT_CHOICES)
    file=models.ImageField(upload_to=save_select_path,validators=[FileExtensionValidator(['jpg','png'])])

    def __str__(self):
        return self.title