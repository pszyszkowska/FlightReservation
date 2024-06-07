from django.db import models
from datetime import date
from django.utils.translation import gettext_lazy
from django_enumfield import enum


class Cabin(enum.Enum):
    ECONOMY = 1
    PREMIUM_ECONOMY = 2
    BUSINESS = 3

    __verbose_names__ = {
        ECONOMY: gettext_lazy("Economy"),
        PREMIUM_ECONOMY: gettext_lazy("Premium Economy"),
        BUSINESS: gettext_lazy("Business"),
    }

    __default__ = ECONOMY


class Country(models.Model):
    countryName = models.CharField(max_length=50, unique=True, verbose_name=gettext_lazy("Country name"))

    def __str__(self):
        return self.countryName


class Airport(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=gettext_lazy("Country name"))
    city = models.CharField(max_length=200, verbose_name=gettext_lazy("City name"))
    iataCode = models.CharField(max_length=3, unique=True, verbose_name=gettext_lazy("Airport code"))

    def __str__(self):
        return "{city} ({iataCode})".format(city=self.city, iataCode=self.iataCode)


class Flight(models.Model):
    departureAirport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departureAirport',
                                         verbose_name=gettext_lazy("Departure airport"))
    arrivalAirport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivalAirport',
                                       verbose_name=gettext_lazy("Arrival airport"))
    departureDate = models.DateField(default=date.today(), verbose_name=gettext_lazy("Departure date"))

    cabin = enum.EnumField(Cabin, default=Cabin.ECONOMY, verbose_name=gettext_lazy("Cabin class"))
    flightNumber = models.CharField(max_length=20, blank=False, null=False, unique=True,
                                    verbose_name=gettext_lazy("Flight number"))

    def __str__(self):
        return ("Departure airport: {departureAirport} "
                "Arrival airport: {arrivalAirport} "
                "Departure Date: {departureDate} "
                "Departure Date: {departureDate}"
                "Cabin: {cabin} "
                "Flight number: {flightNumber}"
                ).format(
            departureAirport=self.departureAirport,
            departureDate=self.departureDate,
            arrivalAirport=self.arrivalAirport,
            cabin=self.cabin,
            flightNumber=self.flightNumber
        )
