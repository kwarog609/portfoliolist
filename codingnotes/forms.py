from django import forms
from django.forms import ModelForm
from .models import Notes
from tinymce.widgets import TinyMCE

class SaveNewNotes(ModelForm):
    class Meta:
        model = Notes
        #fields = ['title', 'tags', "body",]
        fields = '__all__'

        widgets = {
                'title': forms.TextInput(),

                'body': TinyMCE(attrs={'cols': 80, 'rows': 30})
        }