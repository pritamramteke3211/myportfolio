from django.db import models
from datetime import datetime



# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    tag_line = models.CharField(max_length=200)
    s_description = models.TextField()
    l_description = models.TextField()
    lang_used = models.CharField(max_length=200,default='')
    proj_image = models.ImageField(upload_to='images/')
    release = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name
