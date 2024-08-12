from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Trip, Note

class HomeView(TemplateView):
    template_name = 'travel/index.html'

class TripListView(ListView):
    model = Trip
