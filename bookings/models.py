from django.db import models
from django.conf import settings
from rooms.models import Room
from datetime import date






class Booking(models.Model):
    STATUS_CHOICE = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled','Cancelled'),
    )


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status =  models.CharField(max_length=20, choices=STATUS_CHOICE, default='Pending')


    def save(self, *args, **kwargs):
        days = (self.check_out - self.check_in).days
        self.total_price = days * self.room.price
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username} - Room {self.room.room_number}"




    
     