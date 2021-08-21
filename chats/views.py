from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils.datastructures import MultiValueDictKeyError


import uuid

from .forms import *


# Create your views here.


def Fronpage(request):
    return render(request, 'chats/frontpage.html')


@login_required(login_url='login')
def Index(request):
    randROOM = None
    if request.method == "POST":
        randROOM = str(uuid.uuid4().hex)
    return render(request, 'chats/dashboard.html', {'randROOM': randROOM})


@login_required(login_url='login')
def EnterRoom(request):
    if request.method == "POST":
        roomName = request.POST['roomName']
        return redirect('chat/{}'.format(roomName))
    return render(request, 'chats/gotoroom.html')


@login_required(login_url='login')
def SaveRoom(request):
    return render(request, 'chats/savedroom.html')


@login_required(login_url='login')
def Room(request, room_name):
    return render(request, 'chats/room.html', {'room_name': room_name})


def Login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username or Password is Incorrect")

    context = {}
    return render(request, 'chats/login.html')


def Register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account Created For " + user)
                return redirect('login')

    context = {"form": form}
    return render(request, 'chats/register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('frontpage')
