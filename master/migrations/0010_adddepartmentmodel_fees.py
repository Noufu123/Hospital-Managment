# Generated by Django 3.2.9 on 2021-12-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0009_addleaveviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddepartmentmodel',
            name='fees',
            field=models.IntegerField(default=200),
        ),
    ]
