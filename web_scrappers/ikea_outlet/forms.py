from django import forms
from .models import Market, Article, Person, Search


class MarketAddForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market name', max_length=64)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market address', max_length=64)
    webpage = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Market webpage', max_length=128)

class UserAddForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='User name', max_length=64)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Email', max_length=64)

class SearchAddForm(forms.Form):
    email = forms.ModelChoiceField(queryset=Person.objects.all().order_by('username'),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Email')
    market = forms.ModelChoiceField(queryset=Market.objects.all().order_by('name'),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Market')
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Search phrase', max_length=64)
                                     


APROVING_CHOICES = (
        (1, "yes"),
        (2, "no"),
    )


class AprovingForm(forms.Form):
    choice = forms.ChoiceField(choices=APROVING_CHOICES, initial=1, label="Are You sure?")


class ArticlesFilterForm(forms.Form):
    markets = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             queryset=Market.objects.all(),
                                             required=False)
