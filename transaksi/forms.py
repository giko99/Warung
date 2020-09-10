from django.forms import ModelForm

from . import models 

class TransaksiForm(ModelForm):
    class Meta:
        model = models.Transaksi
        exclude = []
        