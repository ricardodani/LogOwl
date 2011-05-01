# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj_example.views.home', name='home'),
    url(r'^music/', include('proj_example.basic.music.urls')),
    url(r'^people/', include('proj_example.basic.people.urls')),
    url(r'^movies/', include('proj_example.basic.movies.urls')),
    url(r'^books/', include('proj_example.basic.books.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

"""
Se o modo debug está ligado, significa que está em ambiente de desenvolvimento,
entao o django passa a servir arquivos estáticos.
"""
if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
        (r'^static/(.*)','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    )
