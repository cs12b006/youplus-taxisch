from django.db import models
from driverapp.models import Driver
from customerapp.models import Customer

# Create your models here.
class Request(models.Model):
    status = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=100)
    req_time = models.DateTimeField(auto_now_add=True)
    raised_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    picked_by = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Request No. %d' % (self.pk)

    """@classmethod
    def create(cls, cust, loc=None):
        instance = cls(raised_by=cust, location=loc)
        return instance"""

    class Meta:
        verbose_name_plural = 'Requests'
