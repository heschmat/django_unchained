
from django.urls import path

from .views import home, job_detail

urlpatterns = [
    path('', home, name= 'home'),
    path('job/<int:pk>/', job_detail, name= 'job-detail')
]

