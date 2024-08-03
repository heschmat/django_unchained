from django.shortcuts import render, get_object_or_404, redirect

from .models import Link

# Create your views here.
def home(req):
    links = Link.objects.all()
    context = {'links': links}
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