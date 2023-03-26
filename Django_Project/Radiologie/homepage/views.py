from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from aplicatie1.models import Location


def home(request):
    return render(request, 'homepage/homepage_index.html')


def about(request):
    return render(request, 'homepage/about.html')


def appointment(request):
    return render(request, 'homepage/appointment.html')


def price(request):
    return render(request, 'homepage/price.html')


def services(request):
    return render(request, 'homepage/services.html')


def team(request):
    return render(request, 'homepage/team.html')


def testimonial(request):
    return render(request, 'homepage/testimonial.html')


def contact(request):
    return render(request, 'homepage/contact.html')


