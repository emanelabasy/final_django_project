"""new_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin 
from articles.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [	
    url(r'^user_action/', include('user_action.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^articles/',include('articles.urls')),
    # url(r'^signin/$',signin),
    url(r'home/$',home),
    url(r'forgetPassword/$',forgetPass),
    url(r'confirm_User/$',confirm_User),
    url(r'reset/$',reset),
    url(r'confirm/$',confirm),
    url(r'^accounts/', include('allauth.urls')),

    # url(r'^logout/$',logout),
    # url(r'^details/(?P<art_id>[0-9]+$)',view_selected_articles),
    # url(r'^all/',view_all_articles),
        
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
