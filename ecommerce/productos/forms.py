from django import forms

class MensajeFormulario(forms.Form):
    mensaje = forms.CharField()
    #fecha = forms.DateTimeField()