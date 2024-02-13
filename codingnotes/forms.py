from django import forms
from django.forms import ModelForm
from .models import Notes


class SaveNewNotes(ModelForm):
    class Meta:
        model = Notes
        #fields = ['title', 'tags', "body",]
        fields = '__all__'
    