from django.db import models


class Ariza(models.Model):
    familya = models.CharField(max_length=255, blank=True)
    ism = models.CharField(max_length=255, blank=True)
    sharif = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    telefon_nomer = models.CharField(max_length=255, blank=True)
    tugatgan_oligoh = models.CharField(max_length=255, blank=True)
    fuqaroligi = models.CharField(max_length=255, blank=True)
    telegram_name = models.CharField(max_length=255, blank=True)
    whatsapp_name = models.CharField(max_length=255, blank=True)
    pasport = models.FileField(upload_to='pasport', blank=True)
    rasm = models.FileField(upload_to='rasm', blank=True)
    diplom = models.FileField(upload_to='diplom', blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)


class Qolanma(models.Model):
    file = models.FileField(upload_to='qolanma', blank=True)




