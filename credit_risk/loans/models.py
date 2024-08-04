from django.db import models

# Create your models here.
class User(models.Model):
    national_id = models.CharField(max_length= 20, unique= True)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.national_id
    
class Loan(models.Model):
    LOAN_STATUS_CHOICES = [
        ('granted', 'Granted'),
        ('reject_pay', 'Reject Payment'),
        ('reject_hist', 'Reject History'),
        ('reject_age', 'Reject Age'),
        ('settled', 'Settled'),
    ]

    application_id = models.AutoField(primary_key= True)
    created_at = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    loan_status = models.CharField(max_length= 20, choices= LOAN_STATUS_CHOICES)

    def __str__(self) -> str:
        return f'Loan {self.application_id} for {self.user.national_id}'
