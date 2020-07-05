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
    get_points_url = "https://api.weather.gov/points/"
    
    if request.method == 'POST':
        cord = request.POST.get('cord')
        pointsRes = requests.get(get_points_url+cord).json() 
        hourlyRes = requests.get(pointsRes['properties']["forecastHourly"]).json()
        temp = hourlyRes["properties"]['periods'][0]['temperature']
        context['temp'] = temp
        return render(request,template_name,context)
    else:
        return render(request,template_name,context)
