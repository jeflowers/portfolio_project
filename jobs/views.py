from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def profile(request):
    jobs = Job.objects # grab jobs from Job objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def detail(request, job_id):
    print(job_id)
    # grab unique job id for job chosen
    # Job is unique job object, displaying details of work done for a specific role.
    # looks in database to determine if there is a job id associated with the work.
    # if not display 404.
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job':job_detail})
