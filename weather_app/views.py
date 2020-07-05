from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from weather_app.models import City

# Create your views here.    
def index(request):
    context = {}
    template_name = 'weather_app/base.html'
    
    if request.method == 'POST':
        city = request.POST.get('city')
        #print(city)
        context['city'] = City.objects.get(name=city)
        #print(context['city'])
        return render(request,template_name,context)
    else:
        return render(request,template_name,context)
