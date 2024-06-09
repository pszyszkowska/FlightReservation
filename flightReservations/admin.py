from django.contrib import admin

from .models import Reservation


# Register your models here.
class FlightReservationAdmin(admin.ModelAdmin):
    admin.site.register(Reservation)
