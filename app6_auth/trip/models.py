from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(default=1)
    # Each trip will be associated with one owner.
    # But each user/owner will have multiple trips.
    # => .ForeignKey()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return f'{self.city} --> {self.owner.username}'


class Note(models.Model):
    TRIP_TYPE = (
        ('general', 'General'),
        ('business', 'Business'),
        ('retreat', 'Retreat'),
        ('layover', 'Layover'),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=25, choices=TRIP_TYPE)
    image_link = models.ImageField(upload_to='notes')
    rating = models.PositiveSmallIntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f'{self.trip.city} -- {self.trip.start_date.year}'
