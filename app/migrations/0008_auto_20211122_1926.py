# Generated by Django 3.2.7 on 2021-11-22 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211023_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='l_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='s_description',
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 26, 31, 947222)),
        ),
        migrations.AlterField(
            model_name='project',
            name='release',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 26, 31, 947222)),
        ),
    ]