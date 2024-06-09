from django.urls import path

from . import views
from flightReservations import views as reservation

urlpatterns = [
    path("reservation/", reservation.createReservation, name="createReservation"),
    path("search/", views.search, name="flightSearchResult"),
    path("allFlights/", views.AllFlights.as_view(), name="allFlights"),
    path("", views.flightSearch, name="flightSearch"),
]
