from django.shortcuts import render
import random

# Create your views here.

def add_two_numbers(x,y):
    """adds two numbers"""
    return x + y

def index(request):
    return render(request, "mentaldrill/index.html",{
    })

def startgame(request):
    choice = []
    if request.method == "POST":
        num1 = random.randint(1,10)     #int(request.POST['num1'])
        num2 = random.randint(1,10)     #int(request.POST['num2'])
        ans = add_two_numbers(num1, num2)
        choice.append(ans)
        choice.append(ans + random.randint(1,10))
        choice.append(ans - random.randint(1,2))
        return render(request, "mentaldrill/index.html",{
        "answer": ans,
        'num1': num1,
        'num2': num2,
        'choice': choice,
        })
    else:
        return render(request, "mentaldrill/index.html",{
        })

