from django.db import models
from datetime import datetime

class Transaksi(models.Model):
    waktu = models.DateField(default=datetime.now)
    jumlah = models.IntegerField(default='')
    ket = models.TextField(default='')
