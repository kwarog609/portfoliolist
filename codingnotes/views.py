from django.shortcuts import render
import logging
from .models import Notes
from .forms import CreateNewNotes
# Create your views here.
logger = logging.getLogger(__name__)

notes = Notes.objects.all

def index(request):

    return render(request, "codingnotes/index.html",{
        "notes": notes,
        "forms": CreateNewNotes()


    })

def search_tags(request):
    return render(request, "codingnotes/index.html",{
        "notes": notes,

    })

def create_new_notes():
    pass
