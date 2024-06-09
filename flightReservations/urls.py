from django.urls import path

from . import views

urlpatterns = [
    path("reservations/", views.fetchReservations, name="fetchReservation"),
]
