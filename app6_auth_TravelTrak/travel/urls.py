from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('dashboard/', views.TripListView.as_view(), name= 'trip-list'),
    path('dashboard_func/', views.list_trip, name= 'list-trip'),
    path('dashboard/trip/create', views.TripCreateView.as_view(), name= 'trip-create'),
]

