from django.contrib import admin
from .models import Company_R, Company_Rules_Fin, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments, User, Managers, Users_Vactions, User_Attendance,  User_Rating, User_notfactions
# Register your models here.
admin.site.register(Company_R)
admin.site.register(Financial)
admin.site.register(Notfactions)
admin.site.register(Rating)
admin.site.register(Vacations)
admin.site.register(Attendance)
admin.site.register(Positions)
admin.site.register(Departments)
admin.site.register(User)
admin.site.register(Managers)
admin.site.register(Users_Vactions)
admin.site.register(User_Attendance)
admin.site.register(Company_Rules_Fin)
admin.site.register(User_Rating)
admin.site.register(User_notfactions)
