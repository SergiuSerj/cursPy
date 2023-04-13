import http.client

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import random
import string

from dashbord.forms import UpdateFormDoctor, PacientCreationForm, AppointmentForm, NewAccountFormDoctor, \
    PatientUpdateForm
from dashbord.models import Doctor, Patient, Appointment

# Create your views here.

class OnlyPatientMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check condition here
        if not hasattr(request.user, 'patient'):
            raise Http404("No access to this page")
        return super().dispatch(request, *args, **kwargs)

class OnlyDoctorMixin:
    def dispatch(self, request, *args, **kwargs):
        # Check condition here
        if not hasattr(request.user, 'doctor'):
            raise Http404("No access to this page")
        return super().dispatch(request, *args, **kwargs)

"""varianta 1"""

@login_required
def home(request):
    appointmentsCount = Appointment.objects.count()
    doctorsCount = Doctor.objects.count()
    patientsCount = Patient.objects.count()
    return render(request, 'dashbord/dashbord_principala.html', {'appointments': appointmentsCount, 'doctors': doctorsCount, 'patients': patientsCount})

class RegisterPatient(CreateView):
    model = Patient
    form_class = PacientCreationForm
    template_name = 'dashbord/Pacient/register.html'

    def get_success_url(self):
        return reverse('login')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

class ListDoctorView(ListView):
    model = Doctor
    template_name = 'dashbord/doctor/doctor_list.html'

class CreateDoctorView(CreateView):
    model = Doctor
    template_name = 'dashbord/doctor/doctor_form.html'
    form_class = NewAccountFormDoctor

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')

class ConfirmDoctorAppointment(LoginRequiredMixin, OnlyDoctorMixin, View):
    def get(self, request, pk):
        Appointment.objects.filter(id=pk).update(confirmed=True)
        return redirect('dashbord:Appointment_view')
    

class UpdateDoctorView(LoginRequiredMixin, OnlyDoctorMixin, View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        user = doctor.user
        if request.user.doctor.id != pk:
            raise Http404("Cannot update this doctor")
        form = UpdateFormDoctor(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'service': doctor.service,
            'price': doctor.price
        })
        return render(request, 'dashbord/doctor/doctor_form.html', {'form': form})
    def post(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        user = doctor.user
        form = UpdateFormDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('dashbord:dashbord_index')


class CreatePacientView (CreateView):
    model = Patient
    form_class = PacientCreationForm
    template_name = 'dashbord/Pacient/create.html'

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class UpdatePatientView (LoginRequiredMixin, OnlyPatientMixin, View):
    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        user = patient.user
        if request.user.patient.id != pk:
            raise Http404("Cannot update this doctor")
        form = PatientUpdateForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'address': patient.address,
        })
        return render(request, 'dashbord/Pacient/create.html', {'form': form})
    def post(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        form = PatientUpdateForm(request.POST, instance=patient)
        print(form.errors)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('dashbord:dashbord_index')

class AppointmentCreate(LoginRequiredMixin, OnlyPatientMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'dashbord/Pacient/appoint.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = Doctor.objects.all()
        prices = []
        for doctor in doctors:
            url = f'https://api.exchangerate.host/convert?from=RON&to=EUR&amount={str(doctor.price)}'
            response = requests.get(url)
            data = response.json()
            eurPrice = round(float(data['result']), 2)
            prices.append(eurPrice)
        context['prices'] = prices
        context['doctors'] = doctors
        return context

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')


class AppointmentView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'dashbord/appointment/list.html'

    def get_queryset(self):
        # Filter the queryset to only show appointments for the current user
        # return super().get_queryset().filter(patient=self.request.user)
        #
        # patient_id = self.kwargs.get('patient_id')
        #
        # # Get the patient for the given patient_id
        # patient = get_object_or_404(Patient, id=patient_id)

        # Filter the queryset to only show appointments for the given patient
        # return super().get_queryset().filter(patient=patient)

        if hasattr(self.request.user, 'patient'):
            patient_id = self.request.user.patient.id
            return super().get_queryset().filter(patient_id=patient_id)
        elif hasattr(self.request.user, 'doctor'):
            doctor_id = self.request.user.doctor.id
            return super().get_queryset().filter(doctor_id=doctor_id)
        else:
            return super().get_queryset().none()

    def appointment_list(request):
        return render(request, 'dashbord/appointment/list.html')


    # def appointment_list(request):
    #     appointments = Appointment.objects.all()
    #     return render(request, 'dashbord/appointment/list.html', {'Appointment_view': appointments})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointments = context['appointment_list']
        prices = []
        for appointment in appointments:
            url = f'https://api.exchangerate.host/convert?from=RON&to=EUR&amount={str(appointment.doctor.price)}'
            response = requests.get(url)
            data = response.json()
            eurPrice = round(float(data['result']), 2)
            prices.append(eurPrice)
        context['prices'] = prices
        print(context)
        return context

"""se termina 1"""
# class UpdateDoctorView(UpdateView):
#     model = Doctor
#     template_name = 'dashbord/doctor/doctor_form.html'
#     form_class = UpdateFormDoctor
#
#     def get_object(self, queryset=None):
#         pk = self.kwargs.get('pk')
#         obj = get_object_or_404(self.model, pk=pk)
#         return obj
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         doctor = self.get_object()
#         user = doctor.user
#         kwargs['initial'] = {
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'username': user.username,
#             'email': user.email,
#             'service': doctor.service
#         }
#         kwargs['pk'] = self.kwargs['pk']
#         return kwargs
#
#     def get_success_url(self):
#         return reverse('dashbord:dashbord_index')


""" varianta 2 """