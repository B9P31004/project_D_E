# Generated by Django 3.2.6 on 2021-08-26 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210822_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='class_ID',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='parents_share_ID',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='school_ID',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='school_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='school_share_ID',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='school_year',
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeroom_class', models.IntegerField(null=True)),
                ('class_year', models.IntegerField(null=True)),
                ('school_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school')),
                ('teacher_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.IntegerField()),
                ('student_year', models.IntegerField()),
                ('school_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school')),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parents_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('child_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
    ]
