from django.shortcuts import render
import urllib.parse,urllib.request,urllib.error
import xml.etree.ElementTree as ET
#import City model
from weather_app.models import City
import requests
import json

# View for 'weather/'
def index(request):
    # templates, context, API Url
    context = {}
    template_base = 'weather_app/base.html'
    template_error = 'weather_app/error.html'
    get_points_url = "https://api.weather.gov/points/"
    
    if request.method == 'POST':
        
        if request.POST.get('cord'):        # if search by co-ordinates is selected.
            try:
                cord = request.POST.get('cord')
                pointsRes = requests.get(get_points_url+cord).json() 
                hourlyRes = requests.get(pointsRes['properties']["forecastHourly"]).json()      # Scraping weather details from API 
                temp = hourlyRes["properties"]['periods'][0]['temperature']
                img =  hourlyRes["properties"]['periods'][0]['icon']
                shortDesc = hourlyRes["properties"]['periods'][0]['shortForecast']
                context = {
                    'temp': temp,
                    'img' : img,
                    'desc' : shortDesc
                }   
            except: 
                return render(request,template_error,context)
            
            return render(request,template_base,context)
        
        else:                                  # if search by city is seleceted. 
            try:
                city = request.POST.get('city')
                city_obj = City.objects.get(name=city)
                cord = str(city_obj.latitude) + "," + str(city_obj.longitude)
                pointsRes = requests.get(get_points_url+cord).json() 
                hourlyRes = requests.get(pointsRes['properties']["forecastHourly"]).json()
                temp = hourlyRes["properties"]['periods'][0]['temperature']
                img =  hourlyRes["properties"]['periods'][0]['icon']
                shortDesc = hourlyRes["properties"]['periods'][0]['shortForecast']      # Scraping weather details from API 
                context = {
                    'temp' : temp,
                    'img' : img,
                    'desc' : shortDesc
                }
            except:
                 return render(request,template_error,context)
            
            return render(request,template_base,context)
        
    else:

        return render(request,template_base,context) # If GET method hits.
