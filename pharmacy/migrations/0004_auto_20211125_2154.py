# Generated by Django 3.2.9 on 2021-11-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_pharmacymodel_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacymodel',
            name='expd',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pharmacymodel',
            name='mfd',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pharmacymodel',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pharmacymodel',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
