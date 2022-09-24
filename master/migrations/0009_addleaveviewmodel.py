# Generated by Django 3.2.9 on 2021-12-06 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0008_alter_addappoinmentmodel_appoinment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddLeaveViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('leave_type', models.CharField(choices=[('personalleave', 'personalleave'), ('medicalleave', 'medicalleave'), ('emergencyleave', 'emergencyleave')], max_length=50)),
                ('Start_date', models.DateField(help_text='Please provide thedate in YY/MM/DD')),
                ('end_date', models.DateField(help_text='Please provide thedate in YY/MM/DD')),
                ('approvel_status', models.CharField(choices=[('approve', 'approve'), ('pending', 'pending'), ('reject', 'reject')], max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.adddepartmentmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]