from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

from rideapp.models import Car, Ride 
from django.contrib.auth.models import User
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car 
        fields = '__all__'
        read_only_fileds = ('id')
        extra_kwargs = {"owner": {"required": False}}
class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fileds = ('id', 'rideOwner', 'driverID', 'shareID', 'status')


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')