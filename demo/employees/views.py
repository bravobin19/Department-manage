
from django.shortcuts import render, redirect
from .models import employees as employees_model
from home.models import department as department_model

# Create your views here.


def get_employees(request, id):

    employees_list = employees_model.objects.filter(department_id=id)
    department = department_model.objects.get(department_id=id)
    return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})


def get_employees_form(request):
    department_list = department_model.objects.filter()
    return render(request, 'employeesform.html', {'department_list': department_list})


def add_employees(request):

    department_id = request.POST['department']
    name = request.POST['fullName']
    age = request.POST['age']
    avatar = request.FILES['avatar']
    cv = request.FILES['cv']

    department = department_model.objects.get(department_id=department_id)

    employees = employees_model.objects.create(
        department_id=department,
        name=name,
        avatar=avatar,
        age=age,
        cv=cv,
    )
    employees.save()

    return redirect('/department/'+str(department_id))
