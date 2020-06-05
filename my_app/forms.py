from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'address_complement': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }
        fields = ('address', 'address_complement', 'city', 'state', 'country')
