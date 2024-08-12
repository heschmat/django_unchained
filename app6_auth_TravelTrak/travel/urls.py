from django.urls import path

from .views import HomeView, TripListView

urlpatterns = [
    path('', HomeView.as_view(), name= 'home'),
    path('dashboard/', TripListView.as_view(), name= 'trip-list'),
]
