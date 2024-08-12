from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Trip(models.Model):
    city = models.CharField(max_length= 25)
    country = models.CharField(max_length= 2) # country code
    start_date = models.DateField(blank= True, null= True)
    end_date = models.DateField(blank= True, null= True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'trips')

    def __str__(self):
        return f'{self.owner.username} => {self.city} -- {self.start_date.year}'
    
class Note(models.Model):
    ACTIVITIES = (
        ('event', 'Event'),
        ('retreat', 'Retreat'),
        ('general', 'General'),
    )
    # related_names= 'notes' => to access the notes from a trip: `trip.notes` 
    trip = models.ForeignKey(Trip, on_delete= models.CASCADE, related_name= 'notes')
    title = models.CharField(max_length= 50)
    description = models.TextField()
    type = models.CharField(max_length= 10, choices= ACTIVITIES)
    # uploads the images to the `notes` directory.
    img = models.ImageField(upload_to= 'notes', blank= True, null= True)
    # Set default rating is 3, simply average; ratings {1, 2, 3, 4, 5}
    rating = models.PositiveSmallIntegerField(default= 3, validators= [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.title} @{self.trip.city}'
