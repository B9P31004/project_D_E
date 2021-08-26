from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural='CustomUser'

class School(models.Model):
    school_name=models.CharField(max_length=20,null=False,blank=False)
    
    class Meta:
        verbose_name_plural='School'
    
    def __str__(self):
        return self.school_name

class Student(models.Model):
    student_ID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    school_ID=models.ForeignKey(School,on_delete=models.CASCADE)
    student_class=models.IntegerField(validators=[MinValueValidator(1)],null=False,blank=False)
    student_year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],null=False,blank=False)
    #share_ID=CharField
    #parents_share_ID=models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name_plural='Student'

    def __str__(self):
        return str(self.student_ID)

class Teacher(models.Model):
    teacher_ID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    school_ID=models.ForeignKey(School,on_delete=models.CASCADE)
    homeroom_class=models.IntegerField(validators=[MinValueValidator(1)],null=True,blank=False)
    class_year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],null=True,blank=False)

    class Meta:
        verbose_name_plural='Teacher'

class Parents(models.Model):
    parents_ID=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    child_ID=models.ForeignKey(Student,on_delete=models.CASCADE)
    #share_ID=CharField

    class Meta:
        verbose_name_plural='Parents'
