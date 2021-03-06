"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

#import more than 2 defs,must use","
#from mysite.views import current_datetime,add2
#visit webpage:127.0.0.1:port/*
from mysite import views as mviews

urlpatterns = [
    url(r'^string/$',mviews.current_datetime1,name='string'),
    url(r'^add2/(\d+)/(\d+)/$',mviews.add2,name='add2'),
    url(r'^time/$',mviews.current_datetime,name='time'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', mviews.index,name='home'),
]