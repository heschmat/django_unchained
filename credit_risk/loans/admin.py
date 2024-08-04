from django.contrib import admin

from .models import User, Loan
# Register your models here.

class LoanAdmin(admin.ModelAdmin):
    list_display = ('application_id', 'user', 'loan_status', 'created_at')
    fields = ('user', 'loan_status', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(User)
admin.site.register(Loan, LoanAdmin)
