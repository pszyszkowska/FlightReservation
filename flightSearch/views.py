from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight
from django.views import generic
from .forms import FlightSearchFormRoundTrip, FlightSearchFormOneWay
import datetime


class FlightSearchResultView(generic.DetailView):
    model = Flight
    template_name = 'flightSearchResult.html'


def createReservation(request):
    global resp
    if request.method == 'POST':
        if 'inbound' in request.POST:
            resp = "Outbound: {outbound} Inbound: {inbound}".format(outbound=request.POST['outbound'],
                                                                    inbound=request.POST['inbound'])
        else:
            resp = "Outbound: {outbound}".format(outbound=request.POST['outbound'])
    return HttpResponse(resp)


def search(request):
    template_name = 'flightList.html'
    if request.method == "POST":
        # sprawdzenie rodzaju lotu
        if request.POST.get('flightType') == 'roundTrip':
            formRoundTrip = FlightSearchFormRoundTrip(request.POST)
            if formRoundTrip.is_valid():
                # dodanie zakresu daty +7 dni od podanej przez klienta
                providedDepartureDate = formRoundTrip.cleaned_data['departureDate']
                departureRange = providedDepartureDate + datetime.timedelta(days=7)

                providedArrivalDate = formRoundTrip.cleaned_data['arrivalDate']
                arrivalRange = providedArrivalDate + datetime.timedelta(days=7)

                # flitrowanie dostepnych lotow na podstawie kryteriow z requesta (z forma)
                outbounds = Flight.objects.filter(departureAirport=formRoundTrip.cleaned_data['originIata'],
                                                  arrivalAirport=formRoundTrip.cleaned_data['destinationIata'],
                                                  departureDate__gte=providedDepartureDate,
                                                  departureDate__lte=departureRange
                                                  )

                inbounds = Flight.objects.filter(departureAirport=formRoundTrip.cleaned_data['destinationIata'],
                                                 arrivalAirport=formRoundTrip.cleaned_data['originIata'],
                                                 departureDate__gte=providedArrivalDate,
                                                 departureDate__lte=arrivalRange
                                                 )

                return render(request, template_name, {
                    'outbounds': outbounds,
                    'inbounds': inbounds,
                    'flightType': 'RoundTrip'})
        else:
            formOneWay = FlightSearchFormOneWay(request.POST)
            if formOneWay.is_valid():
                # dodanie zakresu daty +7 dni od podanej przez klienta
                providedDepartureDate = formOneWay.cleaned_data['departureDate']
                departureRange = providedDepartureDate + datetime.timedelta(days=7)

                # flitrowanie dostepnych lotow na podstawie kryteriow z requesta (z forma)
                flightList = Flight.objects.filter(departureAirport=formOneWay.cleaned_data['originIata'],
                                                   arrivalAirport=formOneWay.cleaned_data['destinationIata'],
                                                   departureDate__gte=providedDepartureDate,
                                                   departureDate__lte=departureRange
                                                   )
                return render(request, template_name, {'flightList': flightList, 'flightType': 'OneWay'})


class AllFlights(generic.ListView):
    template_name = 'allFlights.html'
    context_object_name = 'flightList'

    def get_queryset(self):
        return Flight.objects.all().order_by('departureDate')


def flightSearch(request):
    template_name = 'flightSearch.html'
    formRoundTrip = FlightSearchFormRoundTrip()
    formOneWay = FlightSearchFormOneWay()

    return render(request, template_name, {"formRoundTrip": formRoundTrip, "formOneWay": formOneWay})
