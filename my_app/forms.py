from django import forms
from .models import STATE_CHOICES


class AddressForm (forms.Form):
    address = forms.CharField(
        max_length=255,
        label='Endereço',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Avenida Paulista, 1000'
            })
    )
    address_complement = forms.CharField(
        max_length=30,
        required=False,
        label='Complemento',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Bloco 10 Apto 44'
            }
        )
    )
    city = forms.CharField(
        max_length=255,
        label='Cidade',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: São Paulo'
            }
        )
    )
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        label='Estado',
        widget=forms.Select(
            attrs={
              'class': 'form-control'
            }
        )
    )
    country = forms.CharField(
        max_length=255,
        label='País',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Brasil'
            }
        )
    )
