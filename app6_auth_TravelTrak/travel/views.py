from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView, CreateView, DetailView
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


class TripDetailView(DetailView):
    template_name = 'travel/trip_detail.html'
    # queryset = Trip.objects.all()
    model = Trip
    context_object_name = 'trip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_trip = context['object']
        # Add the notes for the trip to the context:
        context['notes'] = this_trip.notes.all()
        return context


class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note

    # Filter to show only the notes for the logged-in user:
    def get_queryset(self):
        # To access to the `owner` field of the `trip` (foreign key) use `__`
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset
