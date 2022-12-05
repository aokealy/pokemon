from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Pokemon Cards'},
    {'id': 2, 'name': 'Graded Cards'},
    {'id': 3, 'name': 'Different Pokemon'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request, 'main/room.html', context)
