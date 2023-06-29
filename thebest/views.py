from django.shortcuts import render
from django.views import generic
from thebest.models import Reservation


class ReservationView(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'


def homepage(request):
    return render(request, 'index.html')


def get_menu(request):
    return render(request, 'menu.html')


def get_open_times(request):
    return render(request, 'open_times.html')


def get_confirm(request):
    return render(request, 'confirm.html')