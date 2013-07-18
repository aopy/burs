# -*- coding: utf-8 -*-
from burs.burslar.models import Burslar, Sehirler
from django.shortcuts import render_to_response
from django.template import RequestContext


def goster(request):
    """
    Gibt alle Namen der Städte und der neuesten zehn Stipendien 
    für die Index-Seite zurück.
    """

    sehirler = Sehirler.objects.order_by('sehir')

    burslar = Burslar.objects.order_by('-id')[:10]

    return render_to_response('index.html',
                              {'sehirler': sehirler,
                               'burslar': burslar},
                              context_instance=RequestContext(request))


def sehir_burs(request, sehir):
    """
    Gibt den Namen einer Stadt, alle Stipendiennamen der entsprechenden
    Stadt, und alle Stipendiennamen für die Stadt-Stipendium-Seite zurück.
    """

    sehir = sehir.replace('-', ' ')
    
    isim = Sehirler.objects.get(sehir=sehir)
  
    sehirb = Burslar.objects.filter(sehir__sehir=sehir)

    burslar = Burslar.objects.order_by('isim')

    return render_to_response('sehirdeburs.html',
                              {'sehirb': sehirb,
                               'sehir': isim,
                               'burslar': burslar},
                              context_instance=RequestContext(request))


def burs_detay(request, isim):
    """
    Gibt den Namen, Informationstext, das Kontaktdetail und Logo-Bild 
    eines bestimmten Stipendiums; und alle Stipendiennamen für die 
    Stipendium-Detail-Seite zurück.
    """
    
    isim = isim.replace('-', ' ')

    burs = Burslar.objects.get(isim=isim)

    burs_isim = burs.isim
    burs_bilgi = burs.bilgi
    burs_iletisim = burs.iletisim
    burs_logo = burs.logo

    burslar = Burslar.objects.order_by('isim')

    return render_to_response('bursdetay.html',
                              {'bursi': burs_isim,
                               'bursb': burs_bilgi,
                               'bursil': burs_iletisim,
                               'bursl': burs_logo,
                               'burslar': burslar},
                              context_instance=RequestContext(request))

