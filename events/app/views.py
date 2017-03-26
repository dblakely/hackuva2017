import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Event

def index(request):
    return HttpResponse("<h1>some html</h1>")

def get_events(request):
    events = [event.to_dict() for event in Event.objects.all()]
    response = {
        'events': events,
    }
    return JsonResponse(response)

def viewer(request):
   return render(request, 'home.html', context={'events': Event.objects.all()})
