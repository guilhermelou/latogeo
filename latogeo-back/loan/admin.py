from django.contrib import admin
from .models import Loan
# Register your models here.


class LoanAdmin(admin.ModelAdmin):
    model=Loan


admin.site.register(Loan, LoanAdmin)

