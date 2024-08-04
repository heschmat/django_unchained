from django import forms

from datetime import date

class LoanApplicationForm(forms.Form):
    national_id = forms.CharField(max_length= 20)

    date_of_birth = forms.DateField(widget= forms.SelectDateWidget(years= range(1950, date.today().year + 1)))
