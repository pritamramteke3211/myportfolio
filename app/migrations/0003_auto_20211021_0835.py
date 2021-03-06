# Generated by Django 3.2.8 on 2021-10-21 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211020_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='release',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 8, 35, 25, 907732)),
        ),
    ]
