
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('project/',views.project,name='project'),
    path('contact/',views.contact,name='contact'),
    path('prac/',views.prac,name='prac'),
    path('app/',include('app.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
