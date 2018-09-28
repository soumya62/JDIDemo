from django.db import models
from django.utils import timezone

class Emp(models.Model):
	EMPNO = models.CharField(max_length=50,unique=True,null=True,blank=True)
	EmpBloodGroup = models.CharField(max_length=50,unique=True,null=True)
	EmpContactNo  = models.CharField(max_length=50,unique=True,null=True)
	EmpDOJ  = models.CharField(max_length=50,unique=True,null=True)
	class meta:
		verbose_name_plural='TestData'
		verbose_name='TestData'