from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    olusturulmaTarihi = models.DateTimeField(
            default=timezone.now)
    yayinlamaTarihi = models.DateTimeField(
            blank = True, null = True)
    def yayinla(self):
        self.yayinlamaTarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
