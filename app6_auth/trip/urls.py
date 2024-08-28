from django.urls import path

from . import views

app_name = 'trip'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.list_trip, name='list-trip'),
]
