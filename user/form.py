from django import forms
from .models import Users

class Formic(forms.ModelForm):
    color = forms.CharField(max_length=120,required=True)
    class Meta :
        model = Users
        fields = ['name','email','myfave']
