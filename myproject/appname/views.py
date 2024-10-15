from django.shortcuts import render, redirect
from django.http import HttpResponse
from appname.models import *
from django.contrib import messages
from appname.forms import UserForm, UserAuthForm
from django.contrib.auth import login, authenticate, logout
from datetime import datetime

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserForm()

    return render(
        request,
        template_name = 'register.html',
        context = {'form': form}
    )

def login_user(request):
    if request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.error(request, 'invalid login or password')
    else:
        form = UserAuthForm()

    return render(
        request,
        template_name = 'login.html',
        context = {'form': form}
    )

def logout_user(request):
    logout(request)
    return redirect('main_page')

def main_page(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels,
        'current_user': 'Anonymous',
        }
    if request.user.is_authenticated:
        current_user = request.user
        context['current_user'] = current_user
    
    return render(
        request,
        template_name="basic.html",
        context=context
    )
    
def hotel_page(request, hotel_name):
    hotel = Hotel.objects.get(name=hotel_name)
    rooms = hotel.rooms.all()
    context={
        "hotel":hotel,
        "rooms":rooms,
    }
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            current_user = current_user
            room_id = request.POST.get("room-select")
            room = Room.objects.get(id=room_id)
            reservation_start = request.POST.get("start-time-select")
            reservation_end = request.POST.get("end-time-select")

            reservation_start_s = datetime.strptime(reservation_start, "%Y-%m-%d").date()
            reservation_end_s = datetime.strptime(reservation_end, "%Y-%m-%d").date()

            reservations = Reservation.objects.filter(room=room_id)
            for reservation in reservations:
                if reservation.reservation_start < reservation_end_s and reservation.reservation_end > reservation_start_s:
                    messages.error(request, 'Date is already reservated')
                    break
            else:
                Reservation.objects.create(
                                        reservation_start=reservation_start,
                                        reservation_end= reservation_end,
                                        room=room,
                                        user=current_user)

    return render(
            request,
            template_name="hotel_page.html",
            context=context
    )

def room_page(request, room_id):

    room = Room.objects.get(id=room_id)
    images = room.images.all()
    context={
        "room":room,
        'images':images,
    }

    return render(
            request,
            template_name="room_page.html",
            context=context
    )
