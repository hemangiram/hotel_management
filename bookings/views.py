from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from  .forms import BookingForm
from django.db.models import Q
from django.contrib import messages






@login_required
def create_booking(request):
    if request.user.role != 'customer':
        return redirect('room_list')

    form = BookingForm(request.POST or None)

    if form.is_valid():
        room = form.cleaned_data['room']
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']

        overlapping = Booking.objects.filter(
            room=room,
            check_in__lt=check_out,
            check_out__gt=check_in,
            status__in=['Pending', 'Confirmed']
        ).exists()

        if overlapping:
            messages.error(request, "This room is already booked for selected dates.")
            return render(request, 'bookings/booking_form.html', {'form': form})

        booking = form.save(commit=False)
        booking.user = request.user
        booking.status = "Pending"
        booking.save()

        messages.success(request, "Room booked successfully!")
        return redirect('my_bookings')

    return render(request, 'bookings/booking_form.html', {'form': form})





@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings':bookings})





@login_required
def booking_list(request):
    if request.user.role != 'admin':
        return redirect('room_list')
    

    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings':bookings})




@login_required
def confirm_booking(request,pk):
    if request.user.role != 'admin':
        return redirect('room_list')
    

    booking = get_object_or_404(Booking, pk=pk)
    booking.status = "Confirmed"
    booking.save()
    return redirect('booking_list')





@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.user != booking.user and request.user.role != 'admin':
         return redirect('room_list')


    booking.status = "Cancelled"
    booking.save()
    return redirect('my_bookings')




 










