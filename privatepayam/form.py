from django import forms

from .models import Private

class SendPV(forms.ModelForm):
    class Meta :
        model =Private
        fields = ['matn']
