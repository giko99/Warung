from django import forms 
from pengguna.models import Pengguna

class penggunaForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = "__all__"