# from django.db import models
# from sy.models import Positions, Departments

# # Create your models here.


# class User(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     trans_living_payment_CHOICES = (
#         ('',)
#     )

#     username = models.CharField(
#         max_length=255,   unique=True, blank=True, null=True,)
#     password = models.CharField(max_length=255)
#     fullName = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     phone_number = models.PositiveIntegerField()
#     birthDate = models.DateTimeField(blank=True)
#     gender = models.CharField(
#         max_length=1, choices=GENDER_CHOICES)
#     emp_date = models.DateTimeField(auto_now_add=True)
#     address = models.CharField(max_length=255)
#     is_hr = models.BooleanField(null=True)
#     positions = models.ForeignKey(Positions, on_delete=models.CASCADE)
#     department = models.ForeignKey(Departments, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
