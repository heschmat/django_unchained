from django.urls import path

from . import views

app_name = 'trip'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.list_trip, name='list-trip'),
    path('dashboard/trip/add/', views.TripCreateView.as_view(), name='create-trip'),
    path('dashboard/trip/<int:pk>/', views.TripDetailView.as_view(), name='detail-trip'),
    path('dashboard/trip/<int:pk>/update/', views.TripUpdateView.as_view(), name='update-trip'),
    path('dashboard/trip/<int:pk>/delete/', views.TripDeleteView.as_view(), name='delete-trip'),
    # notes --------------------
    path('dashboard/note/<int:pk>/', views.NoteDetailView.as_view(), name='detail-note'),
    path('dashboard/note/', views.NoteListView.as_view(), name='list-note'),
    path('dashboard/note/add/', views.NoteCreateView.as_view(), name='create-note'),
    path('dashboard/note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='update-note'),
    path('dashbaord/note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete-note'),
]
