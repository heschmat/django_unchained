from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length= 25)
    description = models.TextField()
    company = models.CharField(max_length= 25)
    salary = models.IntegerField()
    is_active = models.BooleanField(default= True)

    def __str__(self) -> str:
        return f'{self.title} -- {self.company}'
