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
        place= place()
        place.name= data_json['name']
        return HttpResponse("successfully created measurement")
       except:
        return HttpResponse("unsuccessfully created measurement. Variable does not exist")
    
