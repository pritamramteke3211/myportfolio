from django.shortcuts import render

# Create your views here.
def apphome(request):
    return render(request,'app/apphome.html')