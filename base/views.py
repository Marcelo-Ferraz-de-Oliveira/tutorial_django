from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Second message'},
    {'id': 3, 'name': 'Thrid message'},
    {'id': 4, 'name': 'Fouth message'},
    {'id': 5, 'name': 'Fifith message'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk): 
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)