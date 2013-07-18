# -*- coding: utf-8 -*-
from django.db import models

class Sehirler(models.Model):
    """
    Ein Model einer Stadt mit Name.
    """

    sehir = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.sehir

    
class Burslar(models.Model):
    """
    Ein Model eines Stipendiums mit Name, Informationen 
    und Kontaktfelder, Logo, und entsprechende Stadt.
    """

    isim = models.CharField(max_length=50)
    bilgi = models.TextField(max_length=500)
    iletisim = models.TextField(max_length=300)
    logo = models.ImageField(blank=True, upload_to='photo/%Y/%m/%d')
    sehir = models.ManyToManyField(Sehirler)

    def __unicode__(self):
        return self.isim
