"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.models import department

from home import views as home
from employees import views as employees
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts.views import SignUpView
from home.views import SearchResultsView


urlpatterns = [
    path('', home.get_home, name="home"),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('department/<int:id>/', employees.get_employees, name="listemployees"),
    path('addEmployeesForm/', employees.get_employees_form),
    path('addEmployees/', employees.add_employees),
    path('editEmployees/<int:id>/', employees.edit_employees),
    path('updateemployees/<int:id>', employees.update_employees),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('addDepartmentForm/', home.get_department_form),
    path('addDepartment/', home.add_department),
    path('deleteEmployees/<int:id>', employees.delete_employees),
    #path('deleteDepartment/', home.delete_department),
    path('delete/<int:id>', home.delete, name='delete'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Qhieu19"
