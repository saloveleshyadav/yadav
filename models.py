from django.db import models


class Employee(models.Model):
    employee_name = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    date_of_birth = models.DateField()
    picture = models.ImageField(upload_to='folder/')


class Department(models.Model):
    department_name = models.CharField(max_length=10)
    manager = models.models.OneToOneField(Employee)


