from django.shortcuts import render, redirect
from django.views import generic
from thebest.models import Reservation


# class ReservationView(generic.ListView):
#     model = Reservation
#     template_name = 'reservation.html'

def get_reservation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        Reservation.objects.create(
            name=name,
            date=date,
            time=time,
            people=people
        )
        return redirect('get_confirm')
    return render(request, 'reservation.html')


def homepage(request):
    return render(request, 'index.html')


def get_menu(request):
    return render(request, 'menu.html')


def get_open_times(request):
    return render(request, 'open_times.html')


def get_confirm(request):
    return render(request, 'confirm.html')
