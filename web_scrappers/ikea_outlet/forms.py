from django import forms
from .models import Category, Market, Article


class MarketAddForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market name', max_length=64)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market address', max_length=64)
    webpage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market webpage', max_length=128)

