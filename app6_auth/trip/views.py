from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)

from .models import Trip


# Create your views here.
class HomeView(TemplateView):
    template_name = './trip/home.html'


def list_trip(request):
    # trips = Trip.objects.all()
    # Filter the list by the logged-in user:
    trips = Trip.objects.filter(owner=request.user)
    context = {'trips': trips}
    return render(request, './trip/trip_list.html', context)
