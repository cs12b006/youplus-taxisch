from django.shortcuts import render
from .models import Request
from .serializers import RequestSerializer
from rest_framework import viewsets

class ReqViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-req_time')
    serializer_class = RequestSerializer

# Create your views here.
# Insert Request object instance given customer
def request_by_customer(customer):
    r = Request.objects.create(raised_by=customer)

# Driver selected to pickup the request
def driver_pickup(driver, request):
    return 1
