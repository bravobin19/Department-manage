from django.shortcuts import render
from .models import department as department_model

# Create your views here.


def get_home(request):
    department_list = department_model.objects.filter().order_by('department_id')
    return render(request, 'home.html', {'department_list': department_list})
