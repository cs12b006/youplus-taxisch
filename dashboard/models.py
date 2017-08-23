from django.db import models
from driverapp.models import Driver
from customerapp.models import Customer

# Create your models here.
class Request(models.Model):
    status = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=100)
    req_time = models.DateField()
    raised_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    picked_by = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
