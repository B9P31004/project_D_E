from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

def check_regular_test(value):
    if value!="中間" and value!="期末":
        raise ValidationError('中間か期末を入力してください')

class grades(models.Model):
    choice_year=((1,"1年生"),(2,"2年生"),(3,"3年生"))
    choice_semester=((1,"1学期"),(2,"2学期"),(3,"3学期"))
    choice_regular_test=(("中間","中間"),("期末","期末"))
    UniqueID=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    school_year=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],verbose_name="学年",null=False,blank=False,choices=choice_year)
    semester=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)],verbose_name="学期",null=False,blank=False,choices=choice_semester)
    regular_test=models.CharField(validators=[check_regular_test],max_length=2,verbose_name="中間または期末",null=False,blank=False,choices=choice_regular_test)
    national_language=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="国語",null=False,blank=False)
    math=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="数学",null=False,blank=False)
    english=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="英語",null=False,blank=False)
    social_studies=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="社会",null=False,blank=False)
    science=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="理科",null=False,blank=False)
    music=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="音楽",null=False,blank=False)
    art=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="美術",null=False,blank=False)
    technical_arts_and_home_economics=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="技術・家庭科",null=False,blank=False)
    health_and_physical_education=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],verbose_name="保健体育",null=False,blank=False)

    class Meta:
        verbose_name_plural='test_results'

    def __str__(self):
        return str(self.UniqueID)
