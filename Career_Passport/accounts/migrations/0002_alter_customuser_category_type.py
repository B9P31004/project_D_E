# Generated by Django 3.2.6 on 2021-10-24 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='category_type',
            field=models.ManyToManyField(blank=True, related_name='user_set', related_query_name='user', to='accounts.CategoryType'),
        ),
    ]