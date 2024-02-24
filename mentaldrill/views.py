from django.shortcuts import render
import random, json, math

# Create your views here.
global_level = ['beginner', 'easy','medium','hard',]
global_operator = ['addition','subtraction',]
global_counter = 0
global_score = 0

def add_two_numbers(x,y):
    """adds two numbers"""
    return x + y

def subtract_two_numbers(x,y):
    """subtracts two numbers"""
    return x - y

def choose_operator(operator, x, y):
    if operator == 'addition':
        return add_two_numbers(x,y)
    elif operator == 'subtraction':
        return subtract_two_numbers(x,y)
    else:
        return 0

def process_inputs(request_data):
    """process the input parameters and returns a answer, num2, num3 and choices"""
    level = str.lower(str(request_data['level']))
    operator = str.lower(str(request_data['operator']))
    choice = []
    ans = 0
    choice_deviation = 0
    if level == 'beginner':
        print((request_data['level']))
        num1 = random.randint(1,10)     #int(request.POST['num1'])
        num2 = random.randint(1,10)     #int(request.POST['num2'])
        choice_deviation = random.randint(1,10)
    elif level == 'easy':
        num1 = random.randint(1,20)     #int(request.POST['num1'])
        num2 = random.randint(1,20)     #int(request.POST['num2'])
        choice_deviation = random.randint(1,20)
    elif level == 'medium':
        num1 = random.randint(20,100)     #int(request.POST['num1'])
        num2 = random.randint(20,100)     #int(request.POST['num2'])
        choice_deviation = random.randint(20,80)
    elif level == 'hard':
        num1 = random.randint(500,1000)     #int(request.POST['num1'])
        num2 = random.randint(500,1000)     #int(request.POST['num2'])
        choice_deviation = random.randint(200,800)
    else:
        print("choose level")

    if num2 > num1:
        print("true")
        temp = num1
        num1 = num2
        num2 = temp

    ans = choose_operator(operator, num1, num2)
    choice.append(ans)
    choice.append(ans + choice_deviation)
    choice.append(ans - choice_deviation)
    random.shuffle(choice)

    return int(ans), num1, num2, choice
    
def index(request):
    return render(request, "mentaldrill/index.html",{
        "level": global_level,
        "operator": global_operator,
    })

def startgame(request):
    """starts the game"""
    if request.method == "POST":
        global global_counter, global_score
        print(request.POST)
        global_score = request.POST['score']

        if request.POST['score'] == '': #math.isnan(str(request.POST['score'])):
            global_score = 0
        else:
            global_score = int(request.POST['score'])

        print(global_score)
        global_counter += 1

        request_data = request.POST #request.POST.items
        ans, num1, num2, choice = process_inputs(request_data)
        operator = str(request.POST['operator']).lower()
        print(operator)
        return render(request, "mentaldrill/startgame.html",{
        "answer": ans,
        'num1': num1,
        'num2': num2,
        'choice': choice,
        'chosen_operator': operator,
        'chosen_level': str.lower(str(request_data['level'])),
        "level": global_level,
        "operator": global_operator,
        'counter': global_counter,
        'score': global_score,
        })
    else:
        return render(request, "mentaldrill/index.html",{
        "level": global_level,
        "operator": global_operator,
        })

