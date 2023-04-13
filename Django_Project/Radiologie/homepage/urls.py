from django.urls import path
from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]

