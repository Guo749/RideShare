from django.urls import path, re_path 
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from rideapp import views

# router.register('login', views.LoginView)
# router.register('register', views.RegisterView)


urlpatterns = [
    path('login', views.loginView.as_view()),
    path('register', views.registerView.as_view()),
    path('logout', views.logoutUser),
    re_path(r'^carList/$',  views.carList.as_view()),
    re_path(r'^carList/(?P<pk>[0-9]+)$', views.carDetail.as_view()),
    re_path(r'^rideList/$', views.rideList),
    re_path(r'^rideList/(?P<pk>[0-9]+)$', views.rideDetail),
    re_path(r'^getOwnList/(?P<id>[0-9]+)$', views.getOwnList),
    re_path(r'^getSharedList/(?P<id>[0-9]+)$', views.getSharedList),
    re_path(r'^getOpenList/(?P<id>[0-9]+)$', views.getOpenList),
    re_path(r'^cancelRide/(?P<rideid>[0-9]+)$', views.cancelRide),
    re_path(r'^completeRide/(?P<rideid>[0-9]+)$', views.completeRide),  
    re_path(r'^edituser/(?P<userid>[0-9]+)$', views.editUser),
    re_path(r'^user/(?P<pk>[0-9]+)$', views.getUser.as_view()),
    re_path(r'^carListByFk/(?P<pk>[0-9]+)$', views.getCarbyForeignKey.as_view()),
    re_path(r'^driverFilteredRides/$', views.getMatchedOpenRides),
    re_path(r'^driverConfirmedRides/$', views.getAllConfirmedRides)
    # path('logout', views.logoutHandler),
]
