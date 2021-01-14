# Generated by Django 3.1.4 on 2020-12-22 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reports',
            name='datefounded',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reports',
            name='placefounded',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]