from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import Reservation
from flightSearch.models import Flight


# Create your views here.

def createReservation(request):
    if request.method == 'POST':
        if request.POST['tripType'] == 'RoundTrip':
            flightReservation = Reservation(
                outbound=request.POST['outbound'],
                inbound=request.POST['inbound'],
                tripType=request.POST['tripType'],
                username=request.POST['user']
            )
            flightReservation.save()
        else:
            flightReservation = Reservation(
                outbound=request.POST['outbound'],
                inbound=None,
                tripType=request.POST['tripType'],
                username=request.POST['user']
            )
            flightReservation.save()
    return redirect("reservations")


def fetchReservations(request):
    template_name = 'reservations.html'
    today = now().date()
    reservations = Reservation.objects.filter(username=request.user)
    inbounds = Flight.objects.filter(flightNumber__in=reservations.values_list('inbound', flat=True))
    outbounds = Flight.objects.filter(flightNumber__in=reservations.values_list('outbound', flat=True))
    flights = inbounds | outbounds

    return render(request, template_name, {'reservations': flights, 'today':today})
