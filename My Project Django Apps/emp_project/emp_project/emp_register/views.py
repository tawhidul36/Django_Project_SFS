from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def emp_list(request):
    context = {'emp_list': Employee.objects.all()}
    return render(request, "emp_register/emp_list.html", context)

def emp_form(request, id=0):
    if request.method == "GET":
        if id == 0:  # Create a new employee
            form = EmployeeForm()
        else:  # Update existing employee
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)
        return render(request, "emp_register/emp_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=emp)

        if form.is_valid():
            form.save()
        return redirect('/emp/list')


def emp_delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/emp/list')