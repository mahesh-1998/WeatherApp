from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.    
def index(request):
    template_name = 'weather_app/base.html'
    return render(request,template_name)
