
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path(route='', view=views.index, name='home'),
    path(route='index.html', view=views.index, name='index'),
    #path(route='index.html', view=views.index, name='index'),
]
