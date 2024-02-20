from django.shortcuts import render
import logging
from .models import Notes, ContentTag
from .forms import SaveNewNotes
from django.db.models import Q

# Create your views here.
logger = logging.getLogger(__name__)

notes = Notes()
tag = ContentTag()

def index(request):
    return render(request, "codingnotes/index.html",{
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
            })
        else:
            print("invalid")
            return render(request, "codingnotes/index.html",{
            })
    elif request.method == 'GET':
        print("this is get")
        return render(request, "codingnotes/createpost.html",{
            "forms": form,
        })

def search_results(request):
    if request.method == 'POST':
        search_text = request.POST.get('search_text') + ""
        notes = Notes.objects.filter(Q(title__contains=search_text) | Q(body__contains=search_text))

        return render(request, "codingnotes/index.html",{
            "notes": notes,

        })

    return render(request, "codingnotes/index.html",{
    })

"""  if search_results in temp_string:
            print("search in title")
        else:
            print("search not in title") """  