from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Anket(models.Model):
    soru = models.CharField(max_length=100)
    yayinTarihi = models.DateTimeField()

    def __unicode__(self):
        return self.soru

class Secenek(models.Model):
    anket = models.ForeignKey(Anket)
    secenek = models.CharField(max_length=100)
    oySayisi = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.secenek
