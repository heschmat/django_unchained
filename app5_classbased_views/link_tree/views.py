from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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

class LinkUpdateView(UpdateView):
    # create a form
    # if GET: render the form
    # if PUT: update & save the new values in our db
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    # template (same as post/form): `model_form.html` (link_form.html)

class LinkDeleteView(DeleteView):
    model = Link
    # take the pi/pk of the object
    # get_object_or_404(model, FILTER)
    # if available => delete & forward the user to some url
    # if not exist, show appropriate message
    model = Link
    success_url = reverse_lazy('link-list')
    # by default form to submit in order to delete the item
    # expects a template: `model_confirm_delete.html`
    
