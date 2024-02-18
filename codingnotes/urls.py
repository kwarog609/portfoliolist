
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path(route='', view=views.index, name='home'),
    path(route='index.html', view=views.index, name='index'),
    path(route='createpost.html', view=views.create_new_notes, name='create_new_notes'),
    path(route='search_results.html', view=views.search_results, name='search_results'),
    #path(route='index.html', view=views.index, name='index'),
]
