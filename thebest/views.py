from django.shortcuts import render, redirect
from django.views import generic
from thebest.models import Reservation
from .forms import ReservationForm


def get_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_confirm')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'reservation.html', context)


def homepage(request):
    return render(request, 'index.html')


def get_menu(request):
    return render(request, 'menu.html')


def get_open_times(request):
    return render(request, 'open_times.html')


def get_confirm(request):
    return render(request, 'confirm.html')
