from django import forms
from .models import Market


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


class ArticlesFilterForm(forms.Form):
    markets = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             queryset=Market.objects.all(),
                                             required=False)
