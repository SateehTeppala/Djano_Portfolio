from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'resume/home.html')

def projects(request):
    return render(request,'resume/projects.html')