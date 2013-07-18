# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from burs.burslar.views import goster, sehir_burs, burs_detay
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'burs.views.home', name='home'),
    # url(r'^burs/', include('burs.foo.urls')),
    url(r'^$', goster),
                       
    url(u'^sehir/(?P<sehir>[\w|\W]+)/$', sehir_burs),

    url(u'^burs/(?P<isim>[\w|\W]+)/$', burs_detay),

    url(u'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
