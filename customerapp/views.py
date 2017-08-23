from django.shortcuts import render
from . import forms
from .models import Customer

# Create your views here.
def raise_request(request):
    if request.method == 'POST':
        form = forms.CustomerRequestForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data["customer_id"]
            Customer.objects.get_or_create(id=d)
    else:
        form = forms.CustomerRequestForm()
    return render(request, 'customerapp.html', {'form': form})
