from django.contrib import admin
from django.db import models
from .models import Car, Ride

admin.site.register(Car)
admin.site.register(Ride)