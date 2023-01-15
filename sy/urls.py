from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

routers = DefaultRouter()
routers.register('RegisterUser', views.UserViewSet)
routers.register('Manage Managers', views.ManagersViewSet)
routers.register('Manage Vacations', views.VacationsViewSet)
routers.register('Manage Rating', views.RatingViewSet)
routers.register('Manage Notfactions', views.NotfactionsViewSet)
routers.register('Manage Financial', views.FinanciaViewSet)
routers.register('Manage Rules_Company', views.RulesViewSet)
routers.register('Manage Review', views.ReviewViewSet)
routers.register('Manage Departments', views.DepartmentsViewSet)
routers.register('Manage Positions', views.PositionsViewSet)
routers.urls

urlpatterns = routers.urls
