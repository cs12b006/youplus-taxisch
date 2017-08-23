from django import forms

class CustomerRequestForm(forms.Form):
    customer_id = forms.IntegerField(label = "Customer ID", required = True, initial="5")
