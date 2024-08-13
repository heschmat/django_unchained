from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from .models import Trip, Note

class HomeView(TemplateView):
    template_name = 'travel/index.html'

class TripListView(ListView):
    model = Trip

    def get_queryset(self):
        # Filter trips by the logged-in user
        return Trip.objects.filter(owner=self.request.user)

# This is the functional equivalent of the above cbv `TripListView`:
def list_trip(req):
    trips = Trip.objects.filter(owner= req.user)
    # class-based views will pass the context via `object_list`
    context = {'object_list': trips}
    return render(req, 'travel/trip_list.html', context= context)
