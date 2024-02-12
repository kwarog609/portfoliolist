from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=300)
    tags = models.CharField(max_length=200) #separate class one title to many tags
    body = models.TextField(max_length=5000)

