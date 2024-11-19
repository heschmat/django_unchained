from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    note = models.TextField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
