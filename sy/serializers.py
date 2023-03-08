from rest_framework import serializers
from .models import Review, User, info_resignation, Company, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments
from .models import Employee
from django.contrib.auth.hashers import make_password
from . import models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import Group


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_hr'] = user.is_hr

        # ...

        return token


def hashPassword(password: str) -> str:
    if not password == None:
        return make_password(password)
    return None


class Companyserializers (serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['companyName', 'address', 'phone', 'email', 'industryType',
                  'establishedDate', 'website', 'startTime', 'endTime', ]


class Financialserializers (serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = ['bouns', 'discount', 'salary', 'accepted', 'pre_payment']


class Notfactionsserializers (serializers.ModelSerializer):
    class Meta:
        model = Notfactions
        fields = ['Announcment_Title', 'Announcment_Content', 'is_read']


class Vacationsserializers (serializers.ModelSerializer):
    class Meta:
        model = Vacations
        fields = ['user_id', 'vacation_type', 'vacation_reason',
                  'vacation_reason1', 'vacation_date', 'status']


class Ratingserializers (serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['Number_rating', 'respect']


class Userserializers(serializers.ModelSerializer):

    def create(self, validtated_data):
        validtated_data['password'] = hashPassword(
            validtated_data['password'])
        user = models.User(**validtated_data)
        user.save()
        if validtated_data['is_hr']:
            group = Group.objects.get(name='HR')
        else:
            group = Group.objects.get(name='Employee')
        user.groups.add(group)
        print('done !')
        return user

    class Meta:
        model = User
        fields = ['is_hr', 'username', 'password',
                  'fullName', 'email', 'birthDate', 'gender']


class Positionsserializers (serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = ['id', 'postions_name']

    def create(self, validated_data):
        return super().create(validated_data)


class Attendanceserializers (serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['attendanceStatus', 'date', 'clockInTime', 'clockInLatitude',
                  'clockInLongitude', 'clockOutTime', 'clockOutLatitude', 'clockOutLongitude']


class Employeeserializers (serializers.ModelSerializer):
    user_id = Userserializers

    class Meta:
        model = Employee
        fields = ['user_id', 'phoneNumber', 'emp_date', 'address', 'workdays',
                  'photo', 'company', 'positions', 'department']


class Departmentsserializers (serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = ['id', 'name', 'company_id']


class Reviewserializers (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'date',
                  'description', 'name', ]


class info_resignationserializers(serializers.ModelSerializer):

    class Meta:
        model = info_resignation
        fields = ['resignation', 'accepted',
                  ]
