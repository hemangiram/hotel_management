from django.db import models





class Room(models.Model):
    ROOM_TYPES=(
        ('Single','Single'),
        ('Double','Double'),
        ('Deluxe','Deluxe'),
        ('Suite','Suite'),

    )

    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)

    

    def __str__(self):
        return f"Room {self.room_number} -{self.room_type}"
    