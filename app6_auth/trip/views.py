from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView, CreateView, UpdateView, DeleteView, DetailView,
)

from .models import Trip, Note


# Create your views here.
class HomeView(TemplateView):
    template_name = './trip/home.html'


def list_trip(request):
    # trips = Trip.objects.all()
    # Filter the list by the logged-in user:
    trips = Trip.objects.filter(owner=request.user)
    context = {'trips': trips}
    return render(request, './trip/trip_list.html', context)


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip:list-trip')
    fields = ['city', 'country', 'start_date', 'duration']
    ## by default it looks for `modelname_form.html`

    def form_valid(self, form):
        # Everytime a form is submitted, this method will run.
        # Hence, we use it to populate the owner as the logged in user.
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    # By default looks for `modelname_detail.html`
    model = Trip

    # Attach the corresponding `notes` for a trip to the context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the current trip.
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('trip:list-note')
    fields = ['title', 'description', 'image_link', 'type', 'rating', 'trip']

    def get_form(self):
        form = super().get_form()
        # Filter the trips to the ones for the logged-in user:
        trips = Trip.objects.filter(owner=self.request.user)
        # User can only create notes for the trips she created.
        form.fields['trip'].queryset = trips
        return form
