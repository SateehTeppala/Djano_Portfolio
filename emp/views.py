from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import Emp

# Create your views here.
def emp_list(request):
    context = {'emp_list':Emp.objects.all()}
    return render(request,'emp/list.html',context)

def emp_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = EmpForm()
        else:
            emp = Emp.objects.get(pk=id)
            form = EmpForm(instance=emp)
        return render(request,'emp/form.html',{'form':form})
    else:
        if id == 0:
            form = EmpForm(request.POST)
        else:
            emp = Emp.objects.get(pk=id)
            form = EmpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/emp/list')

def emp_delete(request,id):
    emp = Emp.objects.get(pk=id)
    emp.delete()
    return redirect('/emp/list')