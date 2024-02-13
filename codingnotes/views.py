from django.shortcuts import render
import logging
from .models import Notes, ContentTag
from .forms import SaveNewNotes

# Create your views here.
logger = logging.getLogger(__name__)

notes = Notes.objects.all
tag = ContentTag.objects.all

def index(request):
    form = SaveNewNotes(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print("forms saved")

    return render(request, "codingnotes/index.html",{
        "notes": notes,
        "tags": tag,
        "forms": form,
    })

def search_tags(request):
    notes = Notes.objects.all()
    return render(request, "codingnotes/index.html",{
        "notes": notes,
    })

def create_new_notes(request):
    form = SaveNewNotes(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, "codingnotes/index.html",{
                "notes": notes,
                "tags": tag,
                "forms": form,
            })
    elif request.method == 'GET':
        return render(request, "codingnotes/createpost.html",{
            "notes": notes,
            "tags": tag,
            "forms": form,
        })
