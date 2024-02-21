"""
URL configuration for portfoliohome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

#add for static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', view=views.index, name='homepage'),
    path('codingnotes/', include('codingnotes.urls')),
    path('mentaldrill/', include('mentaldrill.urls')),
    path('phonicsreading/', include('phonicsreading.urls')),
    path('chesskidtrainer/', include('chesskidtrainer.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('index.html', view=views.index, name='index'),
#    path(route='', view=views.index, name='homepage'),
]

#add for static files
urlpatterns += staticfiles_urlpatterns()