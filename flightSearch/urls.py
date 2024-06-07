from django.urls import path

from . import views

urlpatterns = [
    path("reservation/", views.createReservation, name="createReservation"),
    path("search/", views.search, name="flightSearchResult"),
    path("allFlights/", views.AllFlights.as_view(), name="allFlights"),
    path("", views.flightSearch, name="flightSearch"),
]