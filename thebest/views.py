from django.shortcuts import render
from django.views import generic
from thebest.models import Reservation


class ReservationView(generic.ListView):
    model = Reservation
    template_name = 'reservation.html'


def homepage(request):
    return render(request, 'index.html')

