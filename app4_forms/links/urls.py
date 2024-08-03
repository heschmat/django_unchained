from django.urls import path

from .views import home, root_link

urlpatterns = [
    path('', home, name= 'home'),
    path('<str:link_slug>', root_link, name= 'root-link')
]
