# Generated by Django 3.2.9 on 2021-11-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_id', models.CharField(max_length=50)),
                ('dept_name', models.TextField(max_length=80)),
            ],
        ),
    ]
