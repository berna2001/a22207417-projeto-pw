from django import forms
from .models import Autor, ArtigoReceita

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class ArtigoReceitaForm(forms.ModelForm):
    class Meta:
        model = ArtigoReceita
        fields = '__all__'
