from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

from .models import department as department_model
from employees.models import employees
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.


def get_home(request):
    department_list = department_model.objects.filter().order_by('department_id')
    return render(request, 'home.html', {'department_list': department_list})


class SearchResultsView(ListView):
    model = department_model
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = department_model.objects.filter(
            Q(name__icontains=query) | Q(
                department_id__icontains=query)
        )
        return object_list


def add_department(request):
    if request.method == 'POST':
        name = request.POST['dname']

        department = department_model.objects.create(
            name=name,
        )
        department.save()

        return redirect('/')
    else:
        return render(request, 'error.html')


def get_department_form(request):
    return render(request, 'departmentform.html')


def delete(request, id):
    member = department_model.objects.get(department_id=id)
    member.delete()

    return redirect('/')
