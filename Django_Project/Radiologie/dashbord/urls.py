from django.urls import path
from dashbord import views

app_name = 'dashbord'

urlpatterns = [
    path('', views.home, name='dashbord_index'),
    path('register', views.RegisterPatient.as_view(), name='patient_register'),
    path('doctors/list', views.ListDoctorView.as_view(), name='doctors_list'),
    path('doctors/create', views.CreateDoctorView.as_view(), name='doctors_create'),
    # path('doctors/<int:pk>/update', views.UpdateDoctorView.as_view(), name='doctors_create')
    path('doctors/<int:pk>/update', views.UpdateDoctorView.as_view(), name='doctors_update'),
    path('patient/create', views.CreatePacientView.as_view(), name='Pacient_crete'),
    path('patient/<int:pk>/update', views.UpdatePatientView.as_view(), name='Pacient_update'),
    path('appointment/create', views.AppointmentCreate.as_view(), name='Appointment_create'),
    path('appointment/list', views.AppointmentView.as_view(), name='Appointment_view'),
    path('appointment/<int:pk>/activate/', views.ConfirmDoctorAppointment.as_view(), name='appointment_confirm'),

]