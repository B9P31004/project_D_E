from django.db import models
#from django.conf import settings
from django.contrib.auth import get_user_model
 
# Create your models here.
class Text(models.Model):
    name=models.CharField(verbose_name="名前",max_length=100,null=False,blank=True)
    text=models.CharField(verbose_name="テキスト",max_length=200,null=False,blank=True)

    class Meta:
        verbose_name_plural='analizing_text'
        
class career_passport01_1(models.Model):
    #settings.AUTH_USER_MODEL,
    UniqueID=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    my_current=models.TextField(verbose_name="今の自分（自分の好きなこと・もの、得意なこと・もの、頑張っていることなど）",null=False,blank=True)
    my_PR=models.TextField(verbose_name="私の自己PR（自分のいところ）",null=False,blank=True)
    my_dream=models.TextField(verbose_name="こんな大人になりたい（将来の夢）",null=False,blank=True)
    getting_skills=models.TextField(verbose_name="そのために、つけたい力",null=False,blank=True)
    study_target=models.TextField(verbose_name="学習面の目標",null=False,blank=True)
    for_study_target=models.TextField(verbose_name="そのために",null=False,blank=True)
    life_target=models.TextField(verbose_name="生活面の目標",null=False,blank=True)
    for_life_target=models.TextField(verbose_name="そのために",null=False,blank=True)
    local_target=models.TextField(verbose_name="家庭・地域での目標",null=False,blank=True)
    for_local_target=models.TextField(verbose_name="そのために",null=False,blank=True)
    others_target=models.TextField(verbose_name="その他（習い事・資格取得）の目標",null=False,blank=True)
    for_others_target=models.TextField(verbose_name="そのために",null=False,blank=True)
    
    class Meta:
        verbose_name_plural='career_passport01_1'

class career_passport02(models.Model):

    class Meta:
        verbose_name_plural='career_passport02'

class career_passport03(models.Model):

    class Meta:
        verbose_name_plural='career_passport03'