from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Company, Company_Rules_Fin, Financial, Notfactions, Rating, Vacations, Attendance, Positions, Departments, Employee, Users_Vactions, User_Attendance,  User_Rating, User_notfactions
# Register your models here.
admin.site.register(Company)
admin.site.register(Financial)
admin.site.register(Notfactions)
admin.site.register(Rating)
admin.site.register(Vacations)
admin.site.register(Attendance)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Positions)
admin.site.register(Departments)
admin.site.register(Users_Vactions)
admin.site.register(User_Attendance)
admin.site.register(Company_Rules_Fin)
admin.site.register(User_Rating)
admin.site.register(User_notfactions)


# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     add_fieldsets = (
#         (

#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "password1", "password2", 'email'),
#             },
#         ),
#     )
