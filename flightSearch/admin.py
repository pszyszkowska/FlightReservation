from django.contrib import admin
from .models import Flight, Airport, Country


# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    admin.site.register(Flight)
    admin.site.register(Airport)
    admin.site.register(Country)
