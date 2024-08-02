from django.shortcuts import render

from .models import JobPosting
# Create your views here

def home(req):
    # jobs = JobPosting.objects.all()

    # SELECT * FROM JobPosting WHERE is_active = true
    jobs = JobPosting.objects.filter(is_active= True)
    context = {'jobs': jobs}
    return render(req, './job_board/index.html', context)

def job_detail(req, pk):
    job = JobPosting.objects.get(pk= pk)
    context= {'job': job}
    return render(req, './job_board/job_detail.html', context)
