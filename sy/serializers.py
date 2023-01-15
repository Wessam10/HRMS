from rest_framework import serializers
from .models import Review, Company_R, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments, Managers
from Core.models import User


class Rulesserializers (serializers.ModelSerializer):
    class Meta:
        model = Company_R
        fields = ['time_for_coming', 'living_time', 'disount_daily',
                  'disount_monthly', 'target_monthly']


class Financialserializers (serializers.ModelSerializer):
    # salary = serializers.Userserializers
    # salary_day = salary/30
    # final_Salary = salary_day
    class Meta:
        model = Financial
        fields = ['bouns', 'discount']


class Notfactionsserializers (serializers.ModelSerializer):
    class Meta:
        model = Notfactions
        fields = ['Announcment_Title', 'Announcment_Content']


class Vacationsserializers (serializers.ModelSerializer):
    class Meta:
        model = Vacations
        fields = ['vacation_type', 'vacation_reason',
                  'vacation_reason1', 'vacation_status', 'vacation_date']


class Ratingserializers (serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['Number_rating', 'respect']


class Positionsserializers (serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ['id', 'postions_name']


class Attendanceserializers (serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['name']


class Departmentsserializers (serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ['id', 'name']


class Userserializers (serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id',  'full_name', 'email',
                  'phone_number', 'birth_date', 'gender', 'emp_date', 'address', 'is_hr', 'salary', 'positions', 'department']


class Managersserializers (serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = ['user_id', 'department']


class Reviewserializers (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'date',
                  'description', 'name', ]
