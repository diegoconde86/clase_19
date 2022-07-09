from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField()
    comision = forms.IntegerField()
