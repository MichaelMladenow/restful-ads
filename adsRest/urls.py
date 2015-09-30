from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'adsRest.core.views.show_player'),
	url(r'^player/(?P<tag>[A-Za-z]+)-(?P<id>[0-9]{4})/$', 'adsRest.core.views.show_player'),
    # Examples:
    # url(r'^$', 'adsRest.views.home', name='home'),
    # url(r'^adsRest/', include('adsRest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
