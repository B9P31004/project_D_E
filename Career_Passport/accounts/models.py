from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    school_name=models.CharField(max_length=20,null=True,blank=False)
    school_ID=models.IntegerField(null=True,blank=False)
    school_year=models.IntegerField(null=True,blank=False)
    class_ID=models.IntegerField(null=True,blank=False)
    class Meta:
        verbose_name_plural='CustomUser'
