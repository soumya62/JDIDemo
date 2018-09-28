from django.db import models
from django.utils import timezone

class TestData(models.Model):
	Name = models.CharField(max_length=50,unique=True,null=True,blank=True)
	RollNo = models.CharField(max_length=50,unique=True,null=True)
	Mark  = models.CharField(max_length=50,unique=True,null=True)
	Math  = models.CharField(max_length=50,unique=True,null=True)
	class meta:
		verbose_name_plural='TestData'
		verbose_name='TestData'