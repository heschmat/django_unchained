from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView, CreateView,
)

from .models import Trip, Note

class HomeView(TemplateView):
    template_name = 'travel/index.html'

class TripListView(ListView):
    model = Trip

    def get_queryset(self):
        # Filter trips by the logged-in user
        # i.e., the user that's making the current request.
        return Trip.objects.filter(owner=self.request.user)

# This is the functional equivalent of the above cbv `TripListView`:
def list_trip(req):
    trips = Trip.objects.filter(owner= req.user)
    # class-based views will pass the context via `object_list`
    context = {'object_list': trips}
    return render(req, 'travel/trip_list.html', context= context)

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def form_valid(self, form):
        # owner should be set by default to the logged-in user.
        form.instance.owner = self.request.user
        return super().form_valid(form)
