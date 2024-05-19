from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views
urlpatterns=[
    url(r'^places/', views.PlacesList),
    url(r'^placescreate/$', csrf_exempt(views.PlaceCreate), name='placesCreate'),
    url(r'^createmeasurements/$', csrf_exempt(views.PlaceCreate), name='placesMeasurements'), 


]