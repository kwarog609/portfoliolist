from django.contrib import admin
from .models import Notes, ContentTag #import the classess that you created

# Register your models here.
admin.site.register(Notes)
admin.site.register(ContentTag)