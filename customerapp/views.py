from django.shortcuts import render
from . import forms
from .models import Customer
from dashboard.views import request_by_customer
from rest_framework import serializers, viewsets

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id']

class CustViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Create your views here.
def raise_request(request):
    if request.method == 'POST':
        form = forms.CustomerRequestForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data["customer_id"]
            c, foo = Customer.objects.get_or_create(id=d)
            request_by_customer(c)
    else:
        form = forms.CustomerRequestForm()
    return render(request, 'customerapp.html', {'form': form})
