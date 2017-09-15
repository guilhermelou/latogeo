from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class LoanView(TemplateView):
    template_name = 'collection/loan.html'
