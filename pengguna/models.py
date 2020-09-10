from django.db import models

class Pengguna (models.Model):
    nama = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

