# Generated by Django 3.2.8 on 2021-11-27 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211127_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 13, 47, 26, 990853)),
        ),
        migrations.AlterField(
            model_name='project',
            name='release',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 27, 13, 47, 26, 990853)),
        ),
    ]
