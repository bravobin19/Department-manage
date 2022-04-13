from django.contrib import admin
from .models import employees


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'employees_id',
                    'name', 'age', 'avatar', 'cv')

    search_field = ('name')
    list_filter = ('department_id', 'name')


# Register your models here.
admin.site.register(employees, EmployeesAdmin)
