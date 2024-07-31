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



class BakalavrHujat(models.Model):
    name = models.TextField()
    
class BakalavrBolim(models.Model):
    name = models.TextField()

class BakalavrTolov(models.Model):
    name = models.TextField()

class BakalavrMalumot(models.Model):
    name = models.TextField()



class MagistrHujat(models.Model):
    name = models.TextField()
    
class MagistrBolim(models.Model):
    name = models.TextField()

class MagistrTolov(models.Model):
    name = models.TextField()

class MagistrMalumot(models.Model):
    name = models.TextField()



class PhdHujat(models.Model):
    name = models.TextField()
    
class PhdBolim(models.Model):
    name = models.TextField()

class PhdTolov(models.Model):
    name = models.TextField()

class PhdMalumot(models.Model):
    name = models.TextField()



class DscHujat(models.Model):
    name = models.TextField()
    
class DscBolim(models.Model):
    name = models.TextField()

class DscTolov(models.Model):
    name = models.TextField()

class DscMalumot(models.Model):
    name = models.TextField()


