from django.views.generic import ListView, DetailView, CreateView
from .models import Department, Employee


class DepartmentListView(ListView):
    model = Department


class DepartmentDetailView(DetailView):
    model = Department


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['employee_name', 'department_name']

