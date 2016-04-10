from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    url(r'^index$',index),
    url(r'^signin/$',signin),
    url(r'^home$',home),
    url(r'^login$',login),
    url(r'^email_login$',email_login),
    url(r'^face_login$',face_login),
    url(r'^register$',register),
    url(r'^email_register$',email_register),
    url(r'^face_register$',face_register),
    url(r'^profile$',profile),
    url(r'^update_profile/(?P<user_id>[0-9]+)$',update_profile),
    url(r'^logout$',logout),    
]
