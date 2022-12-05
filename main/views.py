from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Pokemon Cards'},
    {'id': 2, 'name': 'Graded Cards'},
    {'id': 3, 'name': 'Different Pokemon'},
]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')
