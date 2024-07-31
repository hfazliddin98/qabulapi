from django.db import models




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

