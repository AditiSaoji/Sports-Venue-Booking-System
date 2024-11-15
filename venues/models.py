from django.db import models

class Venue(models.Model):
    SPORT_CHOICES = [
        ('Football', 'Football'),
        ('Basketball', 'Basketball'),
        ('Tennis', 'Tennis'),
        ('Cricket', 'Cricket'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=50, choices=SPORT_CHOICES)
    available_time = models.TimeField()
    booking_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_booking_status(self):
        return "Available" if self.booking_status else "Booked"
