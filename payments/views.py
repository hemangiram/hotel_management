from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payment
from .forms import PaymentForm
from bookings.models import Booking




@login_required
def make_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if hasattr(booking,'payment'):
        return redirect('my_bookings')
    

    form = PaymentForm(request.POST or None)

    if form.is_valid():
        payment = form.save(commit=False)
        payment.booking = booking
        payment.amount = booking.total_price
        payment.payment_status = 'completed'
        payment.save()


        return redirect('payment_success')

    return render(request, 'payments/payment_form.html',{'form':form,'booking':booking})







@login_required
def payment_success(request):
    return render(request, 'payments/payment_success.html')




