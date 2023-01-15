from django.db import models
from sy.models import Positions, Departments
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    trans_living_payment_CHOICES = (
        ('',)
    )

    user_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.PositiveIntegerField(null=True)
    birth_date = models.DateTimeField(null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True)
    emp_date = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=255, null=True)
    is_hr = models.BooleanField()
    salary = models.PositiveIntegerField(null=True)
    positions = models.ForeignKey(
        Positions, on_delete=models.CASCADE, related_name='user_postions', null=True)
    department = models.ForeignKey(
        Departments, on_delete=models.DO_NOTHING, related_name='user_department', null=True)
