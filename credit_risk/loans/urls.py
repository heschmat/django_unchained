from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('apply/', views.apply4loan, name= 'apply4loan')
]
