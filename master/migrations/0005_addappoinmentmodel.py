# Generated by Django 3.2.9 on 2021-12-02 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0004_staffregistrationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAppoinmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_time', models.TimeField(help_text='24 Hour Formate')),
                ('appoinment_date', models.DateField(help_text='Please provide thedate in MM/DD/YY')),
                ('status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.adddepartmentmodel')),
                ('doctorname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.staffregistrationmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
