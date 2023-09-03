from django import forms
from .models import Category, Market, Article


class MarketAddForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market name', max_length=64)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market address', max_length=64)
    webpage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market webpage', max_length=128)


APROVING_CHOICES = (
        (1, "yes"),
        (2, "no"),
    )


class AprovingForm(forms.Form):
    choice = forms.ChoiceField(choices=APROVING_CHOICES, initial=1, label="Are You sure?")


class ScrapForm(forms.Form):
    markets = forms.ModelChoiceField(queryset=Market.objects.all(),
                                     widget=forms.CheckboxSelectMultiple,
                                     required=False)
    categories = forms.ModelChoiceField(queryset=Category.objects.all(),
                                     widget=forms.CheckboxSelectMultiple,
                                     required=False)


class CategoryAddForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Category name', max_length=64)
    symbol = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Symbol', max_length=64)
