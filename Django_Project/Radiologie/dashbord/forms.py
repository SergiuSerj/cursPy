from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import TextInput, Select, HiddenInput

from datetime import timedelta, date
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from dashbord.models import Service_choises, Doctor, Patient, Appointment, Time_choises


class NewAccountFormDoctor(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    service = forms.Select(choices=Service_choises)

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'username', 'email', 'service']
        template_name = 'dashbord/doctor/doctor_form.html'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            # 'password': TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'service': Select(attrs={'placeholder': 'Service', 'class': 'form-control'}, choices=Service_choises),
        }

    def save(self, commit=True):
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=self.cleaned_data['username'], password=password)
        user.password = make_password(password)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            doctor = Doctor.objects.create(user=user)
            doctor.service = self.cleaned_data['service']
            doctor.save()
        return user

    def __init__(self, *args, **kwargs):
        super(NewAccountFormDoctor, self).__init__(*args, **kwargs)


class UpdateFormDoctor(NewAccountFormDoctor):
    def save(self, commit=True):
        doctor = self.instance
        doctor.service = self.cleaned_data['service']
        user = doctor.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            doctor.user = user
            doctor.save()
        return doctor


class PacientCreationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)


    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'username', 'email', 'address']
        template_name = 'dashbord/doctor/doctor_form.html'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
        }

    def save(self, commit=True):
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=self.cleaned_data['username'], password=password)
        user.password = make_password(password)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
            patient = Patient.objects.create(user=user)
            patient.address = self.cleaned_data['address']
            patient.save()
        return user


    def __init__(self, *args, **kwargs):
        super(PacientCreationForm, self).__init__(*args, **kwargs)


User = get_user_model()
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'start', 'date', 'patient')
        widgets = {
            'date': forms.SelectDateWidget(
                empty_label="Choose Year, Month and Day",
                years=range(date.today().year, date.today().year+2),
                attrs={'class': 'form-control'}
            ),
            'start': forms.Select(choices=Time_choises, attrs={'class': 'form-control'}),
            'patient': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.all()
        # self.fields['patient_id'].initial = Patient.objects.get(user_id=self.user.id)
        try:
            self.fields['patient'].initial = Patient.objects.get(user_id=self.user.id)
        except Patient.DoesNotExist:
            print(f"No patient found for user with ID {self.user.id}")

    def clean_date(self):
        date = self.cleaned_data.get('date')
        # check if selected day is weekend
        if date.weekday() in [5, 6]:
            raise ValidationError("Weekends are not allowed.")
        # check if the date is not in the past
        if date < timezone.now().date():
            raise ValidationError("Invalid date.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get("doctor")
        start = cleaned_data.get("start")
        date = cleaned_data.get("date")

        if doctor and start and date:
            # check if the selected start time is not taken
            taken_appointments = Appointment.objects.filter(
                doctor=doctor,
                date=date,
                start=start,
                confirmed=True
            ).count()

            if taken_appointments > 0:
                raise ValidationError("This time is already taken.")


""" varianta 2 """