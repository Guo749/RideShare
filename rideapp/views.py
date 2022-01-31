from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
from functools import partial
import json
from logging import exception
from os import stat
from re import I
import threading
from rest_framework.decorators import  api_view
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.response import Response 
from rest_framework import status
from rideapp.models import Car, Ride
from rideapp.serializer import CarSerializer 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse, HttpResponseForbidden, response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .serializer import CarSerializer, RideSerializer, UserSerializer
from django.db.models import Q
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rideapp import serializer


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening

def sendEmail(receiverAddress):
    content = '''
        Hello please check the page for driver info
    '''
    print("-----------")
    print(receiverAddress)
    senderAddress = 'username@qq.com'
    senderPassword = 'password'
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, 'plain'))
    msg['Subject'] = 'Hey, Your Order Has been claimed'
    msg['From'] = senderAddress

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(senderAddress, senderPassword)
    s.sendmail(senderAddress, receiverAddress, msg.as_string())
    print("email sent")

class loginView(APIView):
    # solution for csrf
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # @method_decorator(csrf_exempt)
    def post(self, request):
        print(request.data)
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
         # print('login failed')
        if user is not None:
            print('login success')
            auth_login(request, user)
            print('login success')
            serializer = UserSerializer(user)
            return Response(data=serializer.data)
        return Response(data={'msg': 'username/password wrong'}, status=status.HTTP_401_UNAUTHORIZED)

class registerView(APIView):
    # solution for csrf
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getUser(APIView):
    def get(self, request, pk):
        driver = User.objects.get(pk=pk)
        if driver != None:
            serializer = UserSerializer(driver)
            return Response(data=serializer.data)
        return Response(data={'msg': 'cannot find driver user'}, status=status.HTTP_404_NOT_FOUND)
        
class getCarbyForeignKey(APIView):
    def get(self, request, pk):
        car = Car.objects.filter(owner=pk)
        if car != None:
            serializer = CarSerializer(car, many=True)
            return Response(data=serializer.data) 
        return Response(data={'msg': 'cannot find car'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["get"])
@login_required
def getMatchedOpenRides(request):
    car = Car.objects.filter(owner=request.user)[0]
    # Find all open rides that match car info, capacity, type and specialInfo
    # The ride must not been claimed before
    print("capacity", car.capacity)
    print("otherInfo", car.otherInfo)
    print("currentUser", request.user.username)
    if car != None:
        query = Q(numPeople=car.capacity)
        #  & \
                # Q(otherInfo=car.otherInfo) 
                # & \
                # Q(driverID_isnull = True)
        # TODO car type is same as ride' type
        rides = Ride.objects.filter(query)
        print("good", rides)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data) 
    return Response(data={'msg': 'cannot find any car related to you'}, status=status.HTTP_404_NOT_FOUND)

@api_view(["get"])
@login_required
def getAllConfirmedRides(request):
    # Get all rides whose dirverID is the current user
    rides = Ride.objects.filter(driverID=request.user)
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)

@api_view(["get"])
@login_required
@csrf_exempt
def logoutUser(request):
    logout(request)
    return Response(data={'mesg': 'logout'}, status=status.HTTP_205_RESET_CONTENT)


class carList(APIView):
    """list all the cars, or create a new car
    """
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # @login_required
    def get(self, request):
        # TODO get should add filter to return the current user's car, instead of the all carList
        cars = Car.objects.all().filter(owner=request.user)
        if cars != None:
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            return Response({'msg': 'no car found'}, status=status.HTTP_404_NOT_FOUND)
    # @login_required
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class carDetail(APIView):
    # authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def get_object(self, pk):
        try:
            print(pk)
            car = Car.objects.get(pk=pk)
            return car
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    def put(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['GET', 'POST'])
@login_required
@csrf_exempt
def rideList(request):
    if request.method == 'GET':
        # user get all open ride 
        requestFromDriver = Car.objects.filter(owner=request.user).count()
        query = Q(rideOwner=request.user) \
                    | Q(isJoinable=True) \
                    | Q(driverID=request.user) \
                    | Q(shareID=request.user) 
        # which mean the request is not from a driver
        if requestFromDriver == 0:
            rides = Ride.objects.filter(query)
        else:
            query |= Q(status=0) # expose those open ride to the driver
            rides = Ride.objects.filter(query)
        print(rides)
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RideSerializer(data = request.data, partial=True)
        print(request.data)
        if serializer.is_valid():
            print(request.user)
            serializer.save(rideOwner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@login_required
@csrf_exempt
def rideDetail(request, pk):
    try:
        '''
        # TODO permission only allowed for the following scenarios:
        # TODO (1) open ride for driver
        # TODO (2) ridesharer for this ride
        # TODO (1) rideowner for this ride
        '''
        ride = Ride.objects.get(pk=pk)
    except Ride.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RideSerializer(ride)
        return Response(serializer.data)
    elif request.method == 'PUT': 
        # user join a open ride
        # driver take a ride
        # driver complete a ride
        # user modify a ride info
        if ride.status == 3: # a completed ride cannot be edit any more
            return Response(status=status.HTTP_403_FORBIDDEN)
        # TODO: do the permission check
        old_status = ride.status
        
        serializer = RideSerializer(ride, data=request.data, partial=True)
        new_status = ride.status
        if request.data.get('status') == 2:
            receiver = User.objects.get(pk=ride.rideOwner.id)

            print(receiver.email)
            thread1 = threading.Thread(target=sendEmail(receiver.email))
            thread1.start()

            if(ride.shareID != None):
                sharer   = User.objects.get(pk=ride.shareID.id)
                thread2 = threading.Thread(target=sendEmail(sharer.email))
                thread2.start()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@login_required
@csrf_exempt
def editUser(request, userid):
    print("=====")
    print(request.data.get('username'))
    print("=======")
    #username = request.
    # print(username)
    user = User.objects.get(id=userid)
    print(user)
    
    serializer = UserSerializer(user, data=request.data, partial=True)
    if(serializer.is_valid()):
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    print("reach here?")
    return Response(status=status.HTTP_403_FORBIDDEN)


"""
This is query function used to get all rides this user owned
@param:
    > id: the user id uniquely
"""
@api_view(['GET'])
@login_required
@csrf_exempt
def getOwnList(request, id):
    query = Q(rideOwner=id) 
    rides = Ride.objects.filter(query).exclude(status=3)
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)

"""
This is the query function used to get all rides this user shared
@param:
    > id: the id of the  user who share it uniquely
"""
@api_view(['GET'])
@login_required
@csrf_exempt
def getSharedList(request, id):
    query = Q(shareID=id)
    rides = Ride.objects.filter(query).exclude(status=3)
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@login_required
@csrf_exempt
def getOpenList(request, id):
    """
        logics are:
            rides that are open to join and noone has joined
            and status cannot be complete or claimed

            can the user join it
    """
 # https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django
 # ref
    
    rides = Ride.objects.filter(status=1).exclude(rideOwner=id)
    serializer = RideSerializer(rides, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@login_required
@csrf_exempt
def cancelRide(request, rideid):
    ride = Ride.objects.filter(id=rideid).first()
    serializer = RideSerializer(ride, data=request.data, partial=True)

    print(request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@login_required
@csrf_exempt
def completeRide(request, rideid):
    ride = Ride.objects.filter(id=rideid).first()
    serializer = RideSerializer(ride, data=request.data, partial=True)

    print(request.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  