from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from geopy.distance import distance
from . models import Employee, Departments


class EmployeesByDepartmentMixin:
    def get_employees(self, department_id):
        department = get_object_or_404(Departments, pk=department_id)
        employees = Employee.objects.filter(department=department)
        return employees
