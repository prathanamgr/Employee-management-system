from django.shortcuts import render, redirect,HttpResponse
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>My First Django Project Page</h1>")
#

def home(request):
    return render(request,"home.html")

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
