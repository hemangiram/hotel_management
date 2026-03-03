from django.db import models
from bookings.models import Booking
import uuid



class Payment(models.Model):
    PAYMENT_METHOD = (
        ('Cash','Cash on Arrival'),
        ('Razorpay', 'Razorpay'),
        ('Stripe','Stripe'),
    )


    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed','Completed'),
        ('Failed','Failed'),
        )
    

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS,default='Pending')
    transaction_id = models.CharField(max_length=100, blank=True)



    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = str(uuid.uuid4())
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.booking.user.username} - {self.payment_status}"
    
    