from django.db import models
from django.utils import timezone

class BlogTestData(models.Model):
	BlogTest = models.IntegerField(max_length=50,unique=True,null=True,)
	BloggerName = models.CharField(max_length=50,unique=True,null=True)
	BloggerContactNo  = models.CharField(max_length=50,unique=True,null=True)
	EmpDOJ  = models.CharField(max_length=50,unique=True,null=True)
	class meta:
		verbose_name_plural='TestData'
		verbose_name='TestData'