from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


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
    PRY_PAYMENT_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'), ]

    bouns = models.CharField(max_length=255, choices=bouns_choices, default=0)
    discount = models.IntegerField()
    pre_payment = models.CharField(max_length=255)
    salary = models.PositiveIntegerField()
    accepted = models.CharField(max_length=10, choices=PRY_PAYMENT_CHOICES, default='pending'
                                )

    def calculate_day_salary(self):
        day_salary = self.salary / 30  # divide salary by 30 to get the daily rate
        return day_salary

    def calculate_hour_salary(self):
        day_hour = self.day_salary / 24  # divide salary by 30 to get the daily rate
        return day_hour

    # def accept_pre_payment(self):
    #     self.accepted = 'accepted'
    #     self.save()

    # def reject_pre_payment(self):
    #     self.accepted = 'rejected'
    #     self.save()

    def calculate_salary(self):
        return self.salary - self.discount + self.bonus


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
        ('Bad', 'Bad'),
        ('Good', 'Good'),
        ('Verygood', 'Verygood'),
        ('Perfect', 'Perfect'),
    )
    respect = models.CharField(
        max_length=255, choices=Administrative_hierarchy, default='Good')


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    is_hr = models.BooleanField(default=False)
    username = models.CharField(
        max_length=255,   unique=True)
    password = models.CharField(max_length=255)
    fullName = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, null=True)
    birthDate = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES)

    REQUIRED_FIELDS = ['is_hr']


class Company (models.Model):
    companyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    industryType = models.CharField(max_length=255)
    establishedDate = models.DateTimeField()
    website = models.CharField(max_length=255)
    startTime = models.TimeField()
    endTime = models.TimeField()
    late_time = models.PositiveIntegerField(default=300)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.companyName


class Positions (models.Model):
    company_id = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True)
    postions_name = models.CharField(max_length=255)

    def __str__(self):
        return self.postions_name


class Departments(models.Model):
    company_id = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee (models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=255, unique=True)
    emp_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, null=True)
    workdays = models.CharField(max_length=10, default=list)
    photo = models.ImageField(
        upload_to='employee_photos', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    positions = models.ForeignKey(
        Positions, on_delete=models.CASCADE)
    department = models.ForeignKey(
        Departments, on_delete=models.CASCADE, related_name='employee')


class Notfactions (models.Model):
    Announcment_Title = models.CharField(max_length=255)
    Announcment_Content = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)


class Vacations(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    VACATIONS_TYPE_CHOICES = (
        ('Month', 'Month'),
        ('Day', 'Day'),
        ('Hour', 'Hour'),
    )
    VACATIONS_REASON_CHOICES = (
        ('Sickness', 'Sickness'),
        ('weding', 'weding'),
        ('Mother', 'Mother'),
        ('Holidays', 'Holidays')

    )
    VACATIONS_F_STATE_CHOICES = (
        ('Un Payed', 'Un Payed'),
        ('Payed', 'Payed')


    )

    VACATIONS_STATUS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),


    )
    vacation_type = models.CharField(
        max_length=6, choices=VACATIONS_TYPE_CHOICES)
    vacation_reason = models.CharField(
        max_length=10, choices=VACATIONS_REASON_CHOICES)
    vacation_reason1 = models.CharField(
        max_length=10, choices=VACATIONS_F_STATE_CHOICES)
    vacation_status = models.CharField(
        max_length=255, choices=VACATIONS_STATUS_CHOICES)
    vacation_date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),

    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )


class Attendance(models.Model):
    attendanceStatus = models.CharField(max_length=10)
    date = models.DateField()
    clockInTime = models.DateTimeField(null=True, blank=True)
    clockOutTime = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    name = models.CharField(max_length=255)


class info_resignation(models.Model):
    user_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, blank=True, null=True)
    resignation_CHOICES = (
        ('Yes', 'YES'),
        ('No', 'NO'),
    )

    resignation = models.CharField(max_length=3, choices=resignation_CHOICES)
    accepted = models.BooleanField(default=False)

    def accept_resignation(self):
        self.accepted = True
        self.save()

    def reject_resignation(self):
        self.accepted = False
        self.save()


class Users_Vactions(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vacations_id = models.ForeignKey(Vacations, on_delete=models.CASCADE)


class User_Attendance(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)


class Company_Rules_Fin(models.Model):
    rules_Company = models.ForeignKey(
        Company, on_delete=models.CASCADE)
    financial = models.ForeignKey(Financial, on_delete=models.CASCADE)


class User_Rating(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)


class User_notfactions(models.Model):
    user_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    notfactions = models.ForeignKey(Notfactions, on_delete=models.CASCADE)
