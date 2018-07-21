from django import forms



class PayamForm(forms.Form):
    message = forms.CharField(required = True)
