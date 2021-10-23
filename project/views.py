from django.shortcuts import render
from app.models import Project,Contact
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    context = {'home':'active','projects':projects}
    return render(request, 'home.html',context)

def about(request):
    context = {'about':'active'}
    return render(request, 'about.html',context)

def project(request):
    projects = Project.objects.all()
    context = {'project':'active','projects':projects}
    return render(request, 'project.html',context)

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.message = request.POST['message']

        contact.save()
        messages.success(request,'Thanks For Contact Me. I Will Respond You Soon.')

    context = {'contact':'active'}
    return render(request, 'contact.html',context)

def prac(request):
    context={}
    return render(request, 'prac.html',context)