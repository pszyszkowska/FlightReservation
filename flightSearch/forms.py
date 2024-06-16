import datetime

from django import forms

from flightSearch.models import Airport


class FlightSearchFormRoundTrip(forms.Form):
    model = Airport
    allAirports = Airport.objects.all()
    originIata = forms.ModelChoiceField(queryset=allAirports,
                                        required=True,
                                        initial=allAirports.first(),
                                        label='Origin Airport',
                                        widget=forms.Select(attrs={'class': 'airportselector'})
                                        )

    destinationIata = forms.ModelChoiceField(queryset=allAirports,
                                             required=True,
                                             empty_label='Select Destination',
                                             label='Destination',
                                             widget=forms.Select(attrs={'class': 'airportselector'})
                                             )

    departureDate = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'min': datetime.date.today(),
                'class': 'dateselector'
            }
        ),
        label='Departure Date'
    )

    arrivalDate = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'min': datetime.date.today(),
                'class': 'dateselector'
            }
        ),
        label='Arrival Date'
    )


class FlightSearchFormOneWay(forms.Form):
    model = Airport
    allAirports = Airport.objects.all()
    originIata = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        required=True,
        initial=Airport.objects.first(),
        label = 'Origin Airport',
        widget=forms.Select(attrs={'class': 'airportselector'})
    )

    destinationIata = forms.ModelChoiceField(
        queryset=allAirports,
        required=True,
        empty_label='Select Destination',
        label='Destination',
        widget=forms.Select(attrs={'class': 'airportselector'})
    )

    departureDate = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'min': datetime.date.today(),
                'class': 'dateselector'
            }
        ),
        label='Departure Date',
    )
