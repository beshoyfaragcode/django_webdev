"""beshoy_pythonwebpge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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


 beshoyfarag 
     
       """
from django.conf.urls import url,include

from. import views
from blog import views as blog_views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
   
    url(r'^$',auth_views.login , {'template_name':'beshoy website/home.html'}) ,
    url(r'^about', auth_views.login , {'template_name':'beshoy website/about.html'}) ,
       url(r'^beshoyfarag',auth_views.login , {'template_name':'beshoy website/home.html'}) ,
        url(r'^myschool',auth_views.login , {'template_name':'beshoy website/myschool.html'}) ,
        url(r'^mylif', auth_views.login , {'template_name':'beshoy website/mylif.html'}) ,
        url(r'^home' ,auth_views.login , {'template_name':'beshoy website/todo.html'}) ,
        url(r'^login/$',auth_views.login , {'template_name':'beshoy website/djangologin.html'}) ,
         url(r'^signup', views.signup, name='signup'),
     url(r'^blog.html$', blog_views.blog, name='blog'),
    url(r'^contact/', include('contact_form.urls')),
]