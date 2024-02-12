from django import forms

class CreateNewNotes(forms.Form):
    title = forms.CharField(max_length=300)
    tags = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    

    