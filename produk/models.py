from django.db import models

# Create your models here.
class Produk(models.Model):
    nama = models.CharField(max_length=255)
    jenis = models.CharField(max_length=255)
    stock = models.IntegerField()
    harga = models.IntegerField()