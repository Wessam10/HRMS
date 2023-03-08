from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include
from .views import MyTokenObtainPairView

routers = DefaultRouter()
routers.register('RegisterHr', views.UserViewSet, basename='Hr')
routers.register('RegisterUser', views.EmployeeViewSet)
routers.register('Manage Vacations', views.VacationsViewSet)
routers.register('Manage Rating', views.RatingViewSet)
routers.register('Manage Notfactions', views.NotfactionsViewSet)
routers.register('Manage Financial', views.FinanciaViewSet)
routers.register('Manage Company', views.CompanyViewSet)
routers.register('Manage Review', views.ReviewViewSet)
routers.register('Manage Departments', views.DepartmentsViewSet)
routers.register('Manage Positions', views.PositionsViewSet)
routers.register('Manage resignation', views.resignationViewSet)
routers.register('Manage Attendance', views.AttendanceViewSet)
routers.register('Manage User_Department',
                 views.EmployeesViewSet, basename='Employee')
routers.urls
urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(routers.urls)),
]


routers.urls
