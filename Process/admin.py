from django.contrib import admin

from Process.models import TestData

@admin.register(TestData)
class TestDataAdmin(admin.ModelAdmin):
	list_display = ['RollNo']