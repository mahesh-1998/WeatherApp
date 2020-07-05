from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from weather_app.models import City
import requests
import xml.etree.ElementTree as ET
import urllib.parse,urllib.request,urllib.error
import json

# Create your views here.    
def index(request):
    context = {}
    template_name = 'weather_app/base.html'
    template_error = 'weather_app/error.html'
    get_points_url = "https://api.weather.gov/points/"
    
    if request.method == 'POST':
        if request.POST.get('cord'):
            try:
                cord = request.POST.get('cord')
                pointsRes = requests.get(get_points_url+cord).json() 
                hourlyRes = requests.get(pointsRes['properties']["forecastHourly"]).json()
                temp = hourlyRes["properties"]['periods'][0]['temperature']
                img =  hourlyRes["properties"]['periods'][0]['icon']
                shortDesc = hourlyRes["properties"]['periods'][0]['shortForecast']
                context['temp'] = temp
                context['img'] = img
                context['desc'] = shortDesc
            except:
                return render(request,template_error,context)
            return render(request,template_name,context)
        else:
            try:
                city = request.POST.get('city')
                city_obj = City.objects.get(name=city)
                lat = city_obj.latitude
                lng = city_obj.longitude 
                print(city_obj)
                cord = str(lat) +","+ str(lng)
                print(cord)
                pointsRes = requests.get(get_points_url+cord).json() 
                hourlyRes = requests.get(pointsRes['properties']["forecastHourly"]).json()
                temp = hourlyRes["properties"]['periods'][0]['temperature']
                img =  hourlyRes["properties"]['periods'][0]['icon']
                shortDesc = hourlyRes["properties"]['periods'][0]['shortForecast']
                context['temp'] = temp
                context['img'] = img
                context['desc'] = shortDesc
            except:
                return render(request,template_error,context)
            return render(request,template_name,context)
    else:
        return render(request,template_name,context)
