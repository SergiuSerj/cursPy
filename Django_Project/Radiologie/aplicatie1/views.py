from django.shortcuts import render
from django.views.generic import ListView
from aplicatie1.models import Location


class LocationsView(ListView):
    model = Location
    template_name = 'aplicatie1/locations_index.html'