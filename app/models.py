from django.db import models
from datetime import datetime

from django.utils.translation import activate



# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    lang_used = models.CharField(max_length=200,default='')
    proj_image = models.ImageField(upload_to='images/')
    release = models.DateTimeField(default=datetime.now())
    proj_link = models.URLField(default='', blank=True)
    proj_link_name = models.CharField(default='', max_length=50, blank=True)
    github_url = models.URLField(default='', blank=True)
    number = models.IntegerField(default=0,null=True)
    launch = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name
