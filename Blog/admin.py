from django.contrib import admin

from Blog.models import BlogTestData

@admin.register(BlogTestData)
class BlogTestDatapAdmin(admin.ModelAdmin):
	list_display = ['BlogTest','BloggerName']