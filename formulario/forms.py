from django import forms
from .models import Formulario_francis

class FrancisForm(forms.ModelForm):
    class Meta:
        model = Formulario_francis
        fields = '__all__'
