from django.conf.urls import *
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()
    
urlpatterns = patterns('',
    (r'^resume/(?P<username>[\w\s\d]{0,100})/$', 'mezzanine_resume.views.user_resume'),
    (r'^resume/$', 'mezzanine_resume.views.index')
)