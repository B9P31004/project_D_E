from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,PermissionsMixin,Group,Permission)
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

# Create your models here.
class School(models.Model):
    school_name=models.CharField(max_length=20,null=False,blank=False)
    
    class Meta:
        verbose_name_plural='School'
    
    def __str__(self):
        return self.school_name

class Role(models.Model):
    role=models.CharField(max_length=3)
    groups=models.ManyToManyField(Permission)

    class MEta:
        verbose_name='Role'

    def __str__(self):
        return str(self.role)

class CategoryType(models.Model):
    type_name=models.CharField(max_length=3,blank=True)

    class Meta:
        verbose_name_plural='CategoryType'
    
    def __str__(self):
        return self.type_name

class CustomUserManager(BaseUserManager):
    #use_in_migrations = True
    def create_user(self,user_ID,name,password=None):
        user=self.model(
            user_ID=user_ID,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,user_ID,name,password=None):
        user = self.create_user(
            user_ID=user_ID,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin,models.Model):
    user_ID=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999999999)],primary_key=True)
    name=models.CharField(max_length=20,null=False,blank=False)
    password=models.TextField(max_length=12,null=False,blank=False)
    school_ID=models.ForeignKey(School,on_delete=models.CASCADE,default=0)
    student_year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],null=True,blank=False,default=0)
    student_class=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(30)],null=True,blank=False,default=0)
    category_type=models.ManyToManyField(CategoryType,blank=True)
    role=models.ManyToManyField(Role,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects=CustomUserManager()

    USERNAME_FIELD='user_ID'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return str(self.user_ID)

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_admin:
            return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    

    class Meta:
        verbose_name_plural='CustomUser'

"""class Student(models.Model):
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
        verbose_name_plural='Parents'"""
