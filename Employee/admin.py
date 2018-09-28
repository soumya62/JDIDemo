from django.contrib import admin

from Employee.models import Emp

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
	list_display = ['EMPNO']