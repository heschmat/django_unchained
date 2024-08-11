from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    # this simplifies querying & rendering
    # links = Link.objects.all()
    # return render(req, 'link_tree/home.html', context= {'links': links})
    model = Link
    # by default it'll look for this template: `model_list.html`
    # so, for our app, it'll be: `link_list.html`
    # also by default it'll pass the `context` as `object_list`
    # so, we can access the links like: {% for link in object_list %}

class LinkCreateView(CreateView):
    # create form.py & the form itself
    # if GET return an empty form
    # if POST save the form data to the databae
    model = Link
    # What fields to show in the form:
    fields = '__all__'
    # Where to redirect after creating & saving the link to the db:
    success_url = reverse_lazy('link-list')
    # template: `model_form.html` (link_form.html)