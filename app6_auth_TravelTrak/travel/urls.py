from django.urls import path

from .views import HomeView, TripListView, list_trip

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('dashboard/', TripListView.as_view(), name= 'trip-list'),
    path('dashboard_func/', list_trip, name= 'list-trip'),
]
