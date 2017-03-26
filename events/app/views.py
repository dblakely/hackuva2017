import json

from datetime import datetime

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


def add_event(request):
    name = request.GET['name']
    dt = datetime.strptime(request.GET['datetime'], "%Y-%m-%dT%H:%M:%SZ")
    location_name = request.GET['location_name']
    latitude = float(request.GET['latitude'])
    longitude = float(request.GET['longitude'])
    category = request.GET.get('category')

    Event(
        name=name,
        location_name=location_name,
        datetime=dt,
        longitude=longitude,
        latitude=latitude,
        category=category
    ).save()

    return HttpResponse("success")
