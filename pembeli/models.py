from django.db import models

class Pembeli(models.Model):
    nama = models.CharField( max_length=255)
    alamat = models.TextField(default='')
    telp = models.CharField( max_length=255)