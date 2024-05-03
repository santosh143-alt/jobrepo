from django.shortcuts import render
from jobapp.models import PuneJobs,BangloreJobs,ChennaiJobs,MumbaiJobs
# Create your views here.
def homepage_view(request):
    return render(request,'jobapp/home.html')

def pune_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/punejobs.html',context=my_dict)

def banglore_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/banglorejobs.html',context=my_dict)

def chennai_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/chennaijobs.html',context=my_dict)

def mumbai_view(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobapp/mumbaijobs.html',context=my_dict)