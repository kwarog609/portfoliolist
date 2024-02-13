from django import forms
from django.forms import ModelForm
from .models import Notes
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class SaveNewNotes(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'tags', "body",]
        #fields = '__all__'

        widgets = {
                'title': forms.TextInput(),
                'tags': forms.TextInput(),
                'body': CKEditorWidget(),
        }