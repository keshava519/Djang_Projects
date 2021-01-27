from django.shortcuts import render
from jobApp.models import Job



def index(request):
    return render(request,'jobsApp/index.html')



def jobview(request):
    job_list=Job.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'jobsApp/job.html',context=my_dict)
