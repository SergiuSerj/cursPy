from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse
import random
import string

from dashbord.forms import UpdateFormDoctor, PacientCreationForm, AppointmentForm, NewAccountFormDoctor
from dashbord.models import Doctor, Patient, Appointment

# Create your views here.

"""varianta 1"""
def home(request):
    return render(request, 'dashbord/dashbord_principala.html')


class ListDoctorView(ListView):
    model = Doctor
    template_name = 'dashbord/doctor/doctor_list.html'

class CreateDoctorView(CreateView):
    model = Doctor
    template_name = 'dashbord/doctor/doctor_form.html'
    form_class = NewAccountFormDoctor

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')




def updateDoctorView(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    user = doctor.user

    if request.method == 'POST':
        form = UpdateFormDoctor(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('dashbord:dashbord_index')
    else:
        form = UpdateFormDoctor(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'service': doctor.service
        })
    return render(request, 'dashbord/doctor/doctor_form.html', {'form': form})


class CreatePacientView (CreateView):
    model = Patient
    form_class = PacientCreationForm
    template_name = 'dashbord/Pacient/test.html'

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')


class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'dashbord/Pacient/appoint.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('dashbord:dashbord_index')

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