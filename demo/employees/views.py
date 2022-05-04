
from email import message

from turtle import update
from django.shortcuts import render, redirect
from datetime import datetime
from dateutil import parser

from .models import employees as employees_model
from home.models import department as department_model
from .models import employees
from django.views.generic import TemplateView, ListView
# Create your views here.
from django.db.models import Q


def get_employees(request, id):

    employees_list = employees_model.objects.filter(department_id=id)
    department = department_model.objects.get(department_id=id)
    return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})


def get_employees_form(request):
    department_list = department_model.objects.filter()
    return render(request, 'employeesform.html', {'department_list': department_list})


def add_employees(request):
    context = {
        'error': 0,
        'msg': ''
    }

    if request.method == 'POST':

        department_id = request.POST['department']

        name = request.POST['fullName']
        age = request.POST['age']
        avatar = request.FILES['avatar']
        cv = request.FILES['cv']

        # Check valid name
        # Check length <=255
        if not name:
            context['error'] = 1
            context['msg'] = 'Name not valid'
        # Check Valid age
        if age:
            try:
                age_datetime = parser.parser(age)
            except:
                context['error'] = 1
                context['msg'] = 'Age not valid'
        else:
            context['error'] = 1
            context['msg'] = 'Age not valid'
        #

        #
        if not context['error']:
            department = department_model.objects.get(
                department_id=department_id)

            employees = employees_model.objects.create(
                department_id=department,
                name=name,
                avatar=avatar,
                age=age,
                cv=cv,
            )
            employees.save()
            return redirect('/department/'+str(department_id))

    return render(request, 'error.html', context=context)


def edit_employees(request, id):
    editemployees = employees_model.objects.get(employees_id=id)
    return render(request, "editemployees.html", {"employees": editemployees})


def update_employees(request, id):
    name = request.POST['name']
    avatar = request.FILES.get('avatar')
    cv = request.FILES.get('cv')

    employees = employees_model.objects.get(employees_id=id)

    employees.name = name

    if avatar:
        employees.avatar = avatar

    if cv:
        employees.cv = cv

    employees.save()
    return render(request, "editemployees.html", )


def delete_employees(request, id):
    member = employees_model.objects.get(employees_id=id)
    member.delete()

    return render(request, 'done.html')


class searchemployees(ListView):
    model = employees
    template_name = 'searchemployees.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = employees.objects.filter(
            Q(name__icontains=query) | Q(
                employees_id__icontains=query)
        )
        return object_list
