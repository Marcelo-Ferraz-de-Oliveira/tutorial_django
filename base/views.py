from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Second message'},
#     {'id': 3, 'name': 'Thrid message'},
#     {'id': 4, 'name': 'Fouth message'},
#     {'id': 5, 'name': 'Fifith message'},
# ]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk): 
    #         room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)