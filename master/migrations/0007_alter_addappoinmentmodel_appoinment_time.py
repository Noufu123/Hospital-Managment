# Generated by Django 3.2.9 on 2021-12-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_alter_addappoinmentmodel_appoinment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addappoinmentmodel',
            name='appoinment_time',
            field=models.CharField(choices=[('10:00am to 11:00am', '10:00am to 11:00am'), ('11:00am to 12:00pm', '11:00am to 12:00pm')], max_length=50),
        ),
    ]