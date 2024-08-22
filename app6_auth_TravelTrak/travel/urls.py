from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('dashboard/', views.TripListView.as_view(), name='trip-list'),
    path('dashboard/note/', views.NoteListView.as_view(), name='note-list'),
    path('dashboard_func/', views.list_trip, name='list-trip'),
    path('dashboard/trip/create', views.TripCreateView.as_view(), name='trip-create'),
    path('dashbaord/trip/<int:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('dahsboard/note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail'),
]
