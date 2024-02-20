
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(route='startgame.html', view=views.startgame, name='startgame'),
    path(route='', view=views.index, name='index'),

]
