# Generated by Django 2.2.13 on 2020-06-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaecontrol', '0007_auto_20200616_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timing',
            name='time',
            field=models.TimeField(),
        ),
    ]