from django.forms import ModelForm

from . import models

class PembeliForm(ModelForm):
    class Meta :
        model = models.Pembeli
        exclude=[]