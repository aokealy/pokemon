from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#{'id': 1, 'name': 'Pokemon Cards'},
#{'id': 2, 'name': 'Graded Cards'},
#{'id': 3, 'name': 'Different Pokemon'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'main/room.html', context)


def createRoom(request):
    context = {}
    return render(request, 'main/room_form.html', context)
