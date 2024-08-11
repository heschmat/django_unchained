from django.urls import path

from .views import home, root_link, create_link, create_link_djform

urlpatterns = [
    path('', home, name= 'home'),
    path('<str:link_slug>', root_link, name= 'root-link'),
    path('link/create', create_link, name= 'create-link'),
    path('link/add', create_link_djform, name= 'add-link')
]
