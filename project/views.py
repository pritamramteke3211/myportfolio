from django.shortcuts import render
from app.models import Project,Contact
from django.contrib import messages


def home(request,pk=None):
    projects = Project.objects.filter(launch=True).order_by('number')

    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.message = request.POST['message']
        
        contact.save()
        messages.success(request,'Thanks For Contact Me. I Will Respond You Soon.')

    context = {'home':'active','projects':projects}
    return render(request, 'home.html',context)

def about(request):
    context = {'about':'active'}
    return render(request, 'about.html',context)

def project(request):
    projects = Project.objects.all()
    print(projects)
    context = {'project':'active','projects':projects}
    return render(request, 'project.html',context)

def project_detail(request,id=None):
    project = Project.objects.get(id=id)
    lang = project.lang_used.split(',')
    context = {'project':project, 'lang':lang}
    return render(request, 'project_details.html',context )

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

def food_order(request):
    return render(request,"food_ordering_site.html")

def veternary(request):
    return render(request,"veternary.html")