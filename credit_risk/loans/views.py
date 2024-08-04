from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.utils import timezone

from .forms import LoanApplicationForm
from .models import User, Loan

from datetime import timedelta, date

# Create your views here.
def home(req):
    return render(req, 'loans/home.html')

def apply4loan(req):
    if req.method == 'POST':
        form = LoanApplicationForm(req.POST)

        if form.is_valid():
            national_id = form.cleaned_data['national_id']
            dob = form.cleaned_data['date_of_birth']
            user, created = User.objects.get_or_create(national_id= national_id, defaults= {'date_of_birth': dob})

            today = date.today()
            user_age = today.year - dob.year

            if user_age < 21:
                loan_status = 'reject_age'
            else:
                # Fetch loans in the past 30 days
                recent_loans = Loan.objects.filter(user= user, created_at__gte= timezone.now() - timedelta(days= 30))
                if any(loan.loan_status in ['granted', 'reject_pay'] for loan in recent_loans):
                    loan_status = 'reject_hist'
                else:
                    loan_status = 'granted'

            Loan.objects.create(user= user, loan_status= loan_status)
            return render(req, 'loans/result.html', {'loan_status': loan_status})
        
    else: # GET
        form = LoanApplicationForm()

    return render(req, 'loans/apply.html', {'form': form})



    return render(req, 'loans/apply.html')