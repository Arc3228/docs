from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment
from .forms import DoctorForm, AppointmentForm


@login_required
def doctor_list_view(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'doctor_list.html', context)


@login_required
def add_doctor_view(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = DoctorForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('doctor-list')
        else:
            form = DoctorForm()
        return render(request, 'add_doctor.html', {'form': form})
    else:
        return redirect('doctor-list')


@login_required
def book_appointment_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.doctor = doctor
            appointment.save()
            return redirect('appointment-detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})


@login_required
def my_appointments_view(request):
    appointments = Appointment.objects.filter(user=request.user)
    context = {
        'appointments': appointments
    }
    return render(request, 'my_appointments.html', context)


@login_required
def delete_appointment_view(request, pk):
    if request.user.is_superuser:
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return redirect('my-appointments')
    else:
        return redirect('my-appointments')