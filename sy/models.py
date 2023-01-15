from django.db import models
from django.contrib.auth.models import AbstractUser


class Company_R(models.Model):
    time_for_coming = models.TimeField()
    living_time = models.TimeField()
    disount_daily = models.IntegerField()
    disount_monthly = models.IntegerField()
    target_monthly = models.IntegerField()


class Financial (models.Model):
    bouns_choices = (
        ('0', '0%'),
        ('10', '10%'),
        ('20', '20%'),
        ('30', '30%'),
        ('40', '40%'),
        ('50', '50%'),
        ('60', '60%'),
        ('70', '70%'),
        ('80', '80%'),
        ('90', '90%'),
        ('100', '100%'),)

    bouns = models.CharField(max_length=255, choices=bouns_choices, default=0)
    discount = models.IntegerField()


class Notfactions (models.Model):
    Announcment_Title = models.CharField(max_length=255)
    Announcment_Content = models.CharField(max_length=255)


class Rating (models.Model):
    rating_nu = (
        ('10', '10'),
        ('20', '20'),
        ('30', '30'),
        ('40', '40'),
        ('50', '50'),
        ('60', '60'),
        ('70', '70'),
        ('80', '80'),
        ('90', '90'),
        ('100', '100'),


    )
    Number_rating = models.CharField(
        max_length=255, choices=rating_nu, default=10)
    Administrative_hierarchy = (
        ('B', 'Bad'),
        ('G', 'Good'),
        ('V', 'Verygood'),
        ('I', 'Perfect'),
    )
    respect = models.CharField(
        max_length=255, choices=Administrative_hierarchy, default='Good')


class Vacations(models.Model):
    VACATIONS_TYPE_CHOICES = (
        ('M', 'Month'),
        ('D', 'day'),
        ('H', 'Hour'),
    )
    VACATIONS_REASON_CHOICES = (
        ('S', 'Sickness'),
        ('W', 'weding'),
        ('M', 'Mother'),

    )
    VACATIONS_F_STATE_CHOICES = (
        ('U', 'Un Payed'),
        ('P', 'Payed')


    )

    VACATIONS_STATUS_CHOICES = (
        ('Y', 'yes'),
        ('N', 'No'),


    )
    vacation_type = models.CharField(
        max_length=1, choices=VACATIONS_TYPE_CHOICES)
    vacation_reason = models.CharField(
        max_length=1, choices=VACATIONS_REASON_CHOICES)
    vacation_reason1 = models.CharField(
        max_length=1, choices=VACATIONS_F_STATE_CHOICES)
    vacation_status = models.CharField(
        max_length=255, choices=VACATIONS_STATUS_CHOICES)
    vacation_date = models.DateTimeField(auto_now_add=True)


class Attendance(models.Model):
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(auto_now_add=True)


class Positions (models.Model):
    postions_name = models.CharField(max_length=255)


class Departments(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
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
    phone_number = models.PositiveIntegerField()
    birth_date = models.DateTimeField()
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    emp_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    is_hr = models.BooleanField()
    salary = models.PositiveIntegerField()
    positions = models.ForeignKey(Positions, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING)


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    name = models.CharField(max_length=255)


class Managers (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING)


class Users_Vactions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    vacations_id = models.ForeignKey(Vacations, on_delete=models.DO_NOTHING)


class User_Attendance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(Attendance, on_delete=models.DO_NOTHING)


class Company_Rules_Fin(models.Model):
    rules_Company = models.ForeignKey(
        Company_R, on_delete=models.DO_NOTHING)
    financial = models.ForeignKey(Financial, on_delete=models.DO_NOTHING)


class User_Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rating = models.ForeignKey(Rating, on_delete=models.DO_NOTHING)


class User_notfactions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    notfactions = models.ForeignKey(Notfactions, on_delete=models.DO_NOTHING)
