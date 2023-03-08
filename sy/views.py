from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework .viewsets import ModelViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from django.contrib.gis.geos import Point
from datetime import datetime, time
from django.utils import timezone
import json
from django.views import View
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review, User, info_resignation, Company, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments, Employee
from .serializers import Reviewserializers, Userserializers, info_resignationserializers, Companyserializers, Financialserializers, Notfactionsserializers, Vacationsserializers, Ratingserializers, Positionsserializers, Attendanceserializers, Departmentsserializers, Employeeserializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken


# Create your views here

# @csrf_exempt


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            tokens = serializer.validated_data
            response_data = {

                'user': {
                    'access': tokens['access'],
                    'refresh': tokens['refresh'],
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_hr': user.is_hr,
                    'fullName': user.fullName,
                    # add other fields as needed
                },
                'status': 'success',
                'message': 'Login successful.'
            }
            serializer = Employeeserializers(user)
            return Response(response_data, status=status.HTTP_200_OK)
        response_data = {
            'status': 'error',
            'message': 'Invalid credentials.'
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)


class EmployeeViewSet (ModelViewSet):
    queryset = Employee.objects.all().order_by('pk')
    serializer_class = Employeeserializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']

    @action(detail=False)
    def me(self, request):
        (user, created) = Employee.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = Employeeserializers(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = Employeeserializers(user, data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save
            return Response(serializer.data)

    def create(self, request):
        if request.method == 'POST':
            user = request.data.pop('user')
            employ = request.data['Employee']
            user_seralizer = Userserializers(data=user)

            if user_seralizer.is_valid():
                user_seralizer.save()
            else:
                return Response(user_seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
            employ['user_id'] = User.objects.get(
                email=user_seralizer.data['email']).pk
            employ_seralizer = Employeeserializers(data=employ)
            if employ_seralizer.is_valid():
                employ_seralizer.save()
                return Response(employ_seralizer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(employ_seralizer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post'])
    # def workdays(self, request, pk=None):
    #     data = json.loads(request.body.decode('utf-8'))
    #     workdays = data.get('workdays', [])
    #     employee = self.get_object()
    #     employee.workdays = workdays
    #     employee.save()
    #     return Response({'status': 'success'})

    def delete(self, request, pk):
        user = get_object_or_404(Employee, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def upload_photo(request):
        if request.method == 'POST':
            photo_file = request.FILES.get('photo')
            if photo_file:
                # Save the photo file as an employee photo
                employee = Employee.objects.get(id=request.user.id)
                employee.photo = photo_file
                employee.save()
                photo_url = employee.photo.url
                return JsonResponse({'photo_url': photo_url})
        return JsonResponse({'error': 'Invalid request'})


class DepartmentsViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = Departmentsserializers
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user.id
        if not User.objects.filter(pk=user, is_hr=True).exists:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)

        request.data['company_id'] = Company.objects.get(
            user_id=request.user.id).pk
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('DepartmentsViewSet.retrievem')
        user = request.user.id
        if not User.objects.filter(pk=user, is_hr=True).exists:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)
        company = Company.objects.get(user_id=user)
        departments = Departments.objects.filter(company_id=company.pk)
        serializer = Departmentsserializers(data=departments).data
        return Response(serializer)

        # return super().retrieve(request, *args, **kwargs)

    def delete(self, request, pk):
        departments = get_object_or_404(Departments, pk=pk)
        departments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PositionsViewSet(ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = Positionsserializers

    def delete(self, request, pk):
        positions = get_object_or_404(Positions, pk=pk)
        positions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = Attendanceserializers

    def delete(self, request, pk):
        attendance = get_object_or_404(Attendance, pk=pk)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def check_employee_status(request, employee_id):
        employee = Employee.objects.get(id=employee_id)

        now = timezone.now().astimezone(employee.timezone)

        if now.time() > Company.startTime:
            start_time_diff = (datetime.combine(now.date(), now.time(
            )) - datetime.combine(now.date(), Company.startTime)).total_seconds()
            if start_time_diff > Company.late_time:
                status = "late"
                Financial.calculate_hour_salary - Financial.discount

            else:
                status = "on time"
        else:
            status = "not started yet"

        data = {"employee_id": employee_id, "status": status}
        return JsonResponse(data)


class VacationsViewSet(ModelViewSet):
    queryset = Vacations.objects.all()
    serializer_class = Vacationsserializers

    def create(self, request, *args, **kwargs):
        print(request.user.id)
        request.data._mutable = True
        request.data['user_id'] = request.user.id
        request.data['status'] = 'pending'
        # request.user.id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            ['is_hr' == True]
            request.data[status]
        return super().update(request, *args, **kwargs)

    def delete(self, request, pk):
        vacations = get_object_or_404(Vacations, pk=pk)
        vacations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def accept(self):
        self.status = 'accepted'

        self.save()

    def pending(self):
        self.accepted = 'pending'
        self.save()

    def reject(self):
        self.status = 'rejected'
        self.save()


class RatingViewSet (ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = Ratingserializers

    def delete(self, request, pk):
        rating = get_object_or_404(Rating, pk=pk)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotfactionsViewSet (ModelViewSet):
    queryset = Notfactions.objects.all()
    serializer_class = Notfactionsserializers

    def delete(self, request, pk):
        notfactions = get_object_or_404(Notfactions, pk=pk)
        notfactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FinanciaViewSet (ModelViewSet):
    queryset = Financial.objects.all()
    serializer_class = Financialserializers

    def delete(self, request, pk):
        financial = get_object_or_404(Financial, pk=pk)
        financial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def accept_pre_payment(self):
        self.accepted = 'accepted'
        self.save()

    def pending_pre_payment(self):
        self.accepted = 'pending'
        self.save()

    def reject_pre_payment(self):
        self.accepted = 'rejected'
        self.save()


class CompanyViewSet (ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializers

    def __add_department(self, departments, company_id):
        for department in departments:
            data = {"name": department, "company_id": company_id}
            dep = Departmentsserializers(data=data)
            if dep.is_valid():
                dep.save()

    def __add_position(self, positions, company_id):
        for position in positions:
            data = {"name": position, "company_id": company_id}
            pos = Positionsserializers(data=data)
            if pos.is_valid():
                pos.save()

    def create(self, request, *args, **kwargs):
        print(request.data)
        user = request.user.id
        if not User.objects.filter(pk=user, is_hr=True).exists:
            return Response(data=None, status=status.HTTP_403_FORBIDDEN)
        company_serializer = Companyserializers(data=request.data)
        if not company_serializer.is_valid():
            return Response(data=company_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        company_serializer.save()
        print(company_serializer.data)
        departments = request.data['departments']
        print(departments)
        self.__add_department(departments, company_id=company_serializer.pk)
        positions = request.data['positions']
        print(positions)
        self.__add_position(positions=positions,
                            company_id=company_serializer.pk)
        return super().create(request, *args, **kwargs)

    def delete(self, request, pk):
        company_R = get_object_or_404(Company, pk=pk)
        company_R.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet (ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = Reviewserializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']
    Search_fields = ['full_name']
    ordering_fields = ['user_id', 'full_name']

    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializers

    def employees_in_department(request, name):
        department = Departments.objects.get(name=name)
        employees = Employee.objects.filter(department=department)
        return render(request, 'employees.html', {'employees': employees})


class resignationViewSet (ModelViewSet):
    queryset = info_resignation.objects.all()
    serializer_class = info_resignationserializers

    def delete(self, request, pk):
        review = get_object_or_404(info_resignation, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet (ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializers

    def employee_create(request):
        if request.method == 'POST':
            serializer = Userserializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = get_object_or_404(User, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
