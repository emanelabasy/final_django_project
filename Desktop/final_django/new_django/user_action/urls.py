from django.conf.urls import url

from . import views
# from .views import *
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.details, name='details'),
    url(r'^addBlog/$', views.addBlog, name='addBlog'),
    url(r'^success/$', views.success, name='success'),
    url(r'^like/$', views.like, name='like'),
    url(r'^design/$',views.design,name='design'),
    url(r'^mark/$', views.mark, name='mark'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/(?P<user_id>[0-9]+)$', views.profile, name='profile'),
    # url(r'^addComment/$', views.addComment, name='addComment'),
    # ex: /polls/5/
]