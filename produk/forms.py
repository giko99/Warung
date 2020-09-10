from django.forms import ModelForm

from . import models 

class ProdukForm(ModelForm):
    class Meta:
        model = models.Produk
        exclude = []
        