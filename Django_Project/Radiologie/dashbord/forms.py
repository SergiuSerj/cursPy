from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import TextInput, Select, HiddenInput, NumberInput, PasswordInput, widgets

from datetime import timedelta, date
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from dashbord.models import Service_choises, Doctor, Patient, Appointment, Time_choises
from dashbord.validators import validate_unique_email, validate_unique_username


class NewAccountFormDoctor(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, required=True,
        widget=widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30, required=True,
        widget=widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=30, required=True,
        validators=[validate_unique_username],
        widget=widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
    )
    email = forms.EmailField(
        max_length=254, required=True,
        validators=[validate_unique_email],
        widget=widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'username', 'email', 'price', 'service']
        template_name = 'dashbord/doctor/doctor_form.html'
        widgets = {
            # 'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            # 'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            # 'password': TextInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            # 'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            # 'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'price': NumberInput(attrs={'placeholder': '450', 'class': 'form-control'}),
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
            doctor.price = self.cleaned_data['price']
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
    first_name = forms.CharField(
        max_length=30, required=True,
        widget=widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30, required=True,
        widget=widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=30, required=True,
        validators=[validate_unique_username],
        widget=widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
    )
    email = forms.EmailField(
        max_length=254, required=True,
        validators=[validate_unique_email],
        widget=widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'input_type': 'password', 'class': 'form-control'}),
                               max_length=30, required=True)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'username', 'email', 'address']
        template_name = 'dashbord/doctor/doctor_form.html'
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            # 'password': PasswordInput(attrs={'input_type': 'password', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
        }

    def save(self, commit=True):
        password = self.cleaned_data['password']
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


class PatientUpdateForm(PacientCreationForm):
    password = forms.CharField(widget=forms.HiddenInput,
                               max_length=30, required=False)
    username = forms.CharField(
        max_length=30, required=False,
        validators=[],
        widget=widgets.HiddenInput,
    )
    email = forms.EmailField(
        max_length=254, required=False,
        validators=[],
        widget=widgets.HiddenInput,
    )
    def save(self, commit=True):
        patient = self.instance
        patient.address = self.cleaned_data['address']
        user = patient.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            patient.user = user
            patient.save()
        return patient


User = get_user_model()


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('doctor', 'start', 'date', 'patient')
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'date': widgets.DateInput(
                attrs={
                    'class': 'col-lg-4 col-form-label',
                    'type': 'date',
                    'min': str(date.today()),
                    'max': str(date.today() + timedelta(days=365))
                }),
            'start': forms.Select(choices=Time_choises, attrs={'class': 'form-control'}),
            'patient': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.all()
        self.fields['patient'].initial = Patient.objects.get(user_id=self.user.id)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is None:
            raise ValidationError("Date is required")
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
                start=start
            ).count()

            if taken_appointments > 0:
                raise ValidationError("This time is already taken.")

        return cleaned_data


""" varianta 2 """
