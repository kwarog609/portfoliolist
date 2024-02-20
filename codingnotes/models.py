from django.db import models
#from ckeditor.fields import RichTextField
from tinymce import models as tinymce_models


class ContentTag(models.Model):
    all_tags = models.CharField(max_length=300, unique=True)
# Create your models here.
    
class Notes(models.Model):
    title = models.CharField(max_length=300)
    tags = models.ManyToManyField(ContentTag) #separate class one title to many tags
    body = tinymce_models.HTMLField()


