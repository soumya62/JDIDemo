from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import User
from pytz import common_timezones

class InvoiceData(models.Model):
   InvoiceNumber=models.CharField(max_length=255,  null=True, blank=True)
   TotalAmount=models.CharField(max_length=255,  null=True, blank=True)
   VAT=models.CharField(max_length=255,  null=True, blank=True)
   Date=models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)