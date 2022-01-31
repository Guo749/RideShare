from curses import meta
from lib2to3.pgen2 import driver
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    # the model of the car, like Porshe, Honda
    type               = models.CharField(max_length=30, null = False)

    # the identifier for each car
    licensePlateNumber = models.CharField(max_length=30, null = False, unique=True)

    # how man people can it hold?
    capacity           = models.IntegerField(default=4, null = False)

    # other information
    otherInfo          = models.CharField(max_length=30, null = True)

    owner              = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="car_owner")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Ride(models.Model):
    rideOwner          = models.ForeignKey(User, related_name='rideOwner', on_delete=models.CASCADE)
    driverID           = models.ForeignKey(User, related_name='driverID', on_delete=models.CASCADE, null=True)
    shareID            = models.ForeignKey(User, related_name='shareID', on_delete=models.CASCADE, null=True)
    # destination address
    destAddr           = models.CharField(max_length=30, null = False)

    # the time expected to arrive
    date               = models.DateField(null=False, auto_now=False)
    time               = models.TimeField(null=False, auto_now=False)
    # type               = models.CharField(max_length=50, null = False)
    # how many people in this side
    numPeople          = models.IntegerField(default=1, null = True)

    # can other passengers join this ride ? 
    isJoinable         = models.BooleanField(default=False, null = False)

    # other information
    otherInfo          = models.CharField(max_length=30, null = True)

    # status of the order, is it just start, or is being accepted by driver
    class STATUS_CHOICES(models.IntegerChoices):
        start = 1
        confirmed = 2
        completed = 3 
    status             = models.IntegerField(default=1, null = False, choices=STATUS_CHOICES.choices)