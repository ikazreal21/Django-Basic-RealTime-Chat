from django.shortcuts import render, redirect
import uuid

# Create your views here.


def Index(request):
    randROOM = None
    if request.method == "POST":
        randROOM = str(uuid.uuid4().hex)
    return render(request, 'chats/dashboard.html', {'randROOM': randROOM})


def Room(request, room_name):
    return render(request, 'chats/room.html', {'room_name': room_name})
