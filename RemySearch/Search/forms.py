from django import forms

class BusquedaForm(forms.Form):
    palabra_clave = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control me-2', 'type': 'search', 'placeholder': 'Buscar', 'aria-label': 'Buscar'}))
