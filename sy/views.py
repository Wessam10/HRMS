from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework .viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework.permissions import  IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Review, Company_R, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments,  Managers, User
from .serializers import Reviewserializers, Rulesserializers, Financialserializers, Notfactionsserializers, Vacationsserializers, Ratingserializers, Positionsserializers, Attendanceserializers, Departmentsserializers, Userserializers, Managersserializers
from . permissions import IsAdminOrReadOnly
from django.views.decorators.csrf import csrf_exempt
# Create your views here


# @csrf_exempt
class UserViewSet (ModelViewSet):
    queryset = User.objects.all().order_by('pk')
    serializer_class = Userserializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']
    Search_fields = ['full_name', 'username']
    ordering_fields = ['user_id', 'full_name']
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False)
    def me(self, request):
        (user, created) = User.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = Userserializers(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = Userserializers(user, data=request)
            serializer.is_valid(raise_exception=True)
            serializer.save
            return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentsViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = Departmentsserializers
    # permission_classes = [IsAuthenticated]

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


class ManagersViewSet(ModelViewSet):
    queryset = Managers.objects.all()
    serializer_class = Managersserializers
    # permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        managers = get_object_or_404(Managers, pk=pk)
        managers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VacationsViewSet(ModelViewSet):
    queryset = Vacations.objects.all()
    serializer_class = Vacationsserializers

    def delete(self, request, pk):
        vacations = get_object_or_404(Vacations, pk=pk)
        vacations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class RulesViewSet (ModelViewSet):
    queryset = Company_R.objects.all()
    serializer_class = Rulesserializers

    def delete(self, request, pk):
        company_R = get_object_or_404(Company_R, pk=pk)
        company_R.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet (ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = Reviewserializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user_id']
    Search_fields = ['full_name']
    ordering_fields = ['user_id', 'full_name']
    permission_classes = [IsAdminOrReadOnly]

    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
