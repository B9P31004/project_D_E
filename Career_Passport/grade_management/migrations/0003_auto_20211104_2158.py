# Generated by Django 3.2.6 on 2021-11-04 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade_management', '0002_alter_grades_regular_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='school_year',
            field=models.IntegerField(choices=[(1, '1年生'), (2, '2年生'), (3, '3年生')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='学年'),
        ),
        migrations.AlterField(
            model_name='grades',
            name='semester',
            field=models.IntegerField(choices=[(1, '1学期'), (2, '2学期'), (3, '3学期')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='学期'),
        ),
    ]