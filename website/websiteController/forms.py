from django import forms
from django.forms import ModelForm
from .models import Palaute

class PalauteLomake(forms.ModelForm):
    class Meta:
        model = Palaute
        fields = ('nimi','sposti','palaute')
        labels = {
            'nimi':'',
            'sposti':'',
            'palaute':''
        }
        widgets = {
            'nimi': forms.TextInput(attrs={'class': 'av-nimi av-form-elem'}),
            'palaute': forms.TextInput(attrs={ 'class': 'av-lisatiedot av-form-elem'}),
            'sposti': forms.EmailInput(attrs={'class': 'av-posti av-form-elem'})
        }