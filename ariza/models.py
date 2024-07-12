from django.db import models


class Ariza(models.Model):
    davlat = models.CharField(max_length=255, blank=True)
    viloyat = models.CharField(max_length=255, blank=True)
    manzil = models.CharField(max_length=255, blank=True)
    familya = models.CharField(max_length=255, blank=True)
    ism = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tugatgan_oligoh = models.CharField(max_length=255, blank=True)
    fuqaroligi = models.CharField(max_length=255, blank=True)
    telegram_name = models.CharField(max_length=255, blank=True)
    whatsapp_name = models.CharField(max_length=255, blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)


class Qolanma(models.Model):
    file = models.FileField(upload_to='qolanma', blank=True)