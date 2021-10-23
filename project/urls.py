
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('project/',views.project,name='project'),
    path('contact/',views.contact,name='contact'),
    path('prac/',views.prac,name='prac'),
    path('app/',include('app.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
