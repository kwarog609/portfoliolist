from django.shortcuts import render

from django.templatetags.static import static
import random





global_phonics_list = ['ba','be','bi','bo','bu',]
global_level = ['easy', 'medium', 'hard']
global_num_of_letters = ["1","2","3"]
global_counter = 0
global_score = 0



def read_phonics_file():
    phonics_file = (('assets/phonicsreading/phonicslist.txt'))

    data = []
    with open(phonics_file) as file:
        for line in file:
            data.append(line.replace('\n', ""))
    return data

# Create your views here.
def index(request):
    return render(request, "phonicsreading/index.html",{
    })

def body(request):
    #random.shuffle(list) --returns none
    phonics=read_phonics_file()
    #random.sample(x, len(x)) --returns new array
    choice = random.sample(phonics, len(phonics))
    print(choice)
    question = random.choice(phonics)
     # array of choices
    
    if request.method == 'POST':
        print(phonics)
        request_data = request.POST
        level = request_data['level']
        print(level)
    return render(request,"phonicsreading/body.html",{
        'level': global_level,
        'phonics_list': global_phonics_list,
        'num_of_letter': global_num_of_letters,
        'chosen_level': global_level,
        'counter': global_counter,
        'score': global_score,
        'choice': choice,
        'question': question,
    })