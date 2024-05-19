from django.shortcuts import render
from .models import Place
from django.http import HttpResponse
from django.http import JsonResponse
import json

# Create your views here.
def PlacesList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id','name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method== 'POST':
       try: 
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place= Place()
        place.name= data_json['name']
        return HttpResponse("successfully created place")
       except Exception as e:
        print(e)
        return HttpResponse("unsuccessfully created place. ")
    
