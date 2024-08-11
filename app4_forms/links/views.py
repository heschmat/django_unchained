from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def home(req):
    # req.GET is a dictionary-like object.
    # .get() checks if the key - `show_all` - doesn't exists, returns 'false'.
    show_all = req.GET.get('show_all', 'false').lower() == 'true'
    print('GET => ', req.GET)
    links = Link.objects.order_by('-n_clicks')
    if not show_all:
        # Only show the 3 most clicked links in the homepage
        links = links[:3]

    context = {'links': links, 'show_all': show_all}
    return render(req, 'links/index.html', context)

def root_link(req, link_slug):
    link = get_object_or_404(Link, slug= link_slug)
    link.update_clicks()
    # in this case, we don't want to render anything.
    # we simply want to re-direct the user to the corresponding `url` for the `slug` given:
    # e.g. mysite.com/django-project => https://www.djangoproject.com/
    # we pass the parameter to the view in the template like so: (root-link) is the name for `root_link()` in urls.py
    # href="{% url 'root-link' link.slug %}
    return redirect(link.url)

def create_link(req):
    print(req.POST)
    return render(req, 'links/create.html', {})

def create_link_djform(req):
    if req.method == 'POST':
        # form has data
        form = LinkForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Save the data & return to home page:
            form.save()
            return redirect(reverse('home'))

    else:
        form = LinkForm()
    
    context = {'form': form}
    return render(req, 'links/create.html', context= context)
