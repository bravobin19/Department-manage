from django.contrib import admin
from .models import department

# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'name')
    search_field = ('name')
    list_filter = ('department_id', 'name')


admin.site.register(department, DepartmentAdmin)
