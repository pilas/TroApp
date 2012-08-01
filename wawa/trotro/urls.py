from django.conf.urls import patterns, include, url

urlpatterns = patterns('trotro.views',
		url(r'^$','welcome'),
		url(r'^aboutus/$','aboutus'),
		url(r'^map/$', 'mapper'),
		url(r'^search/$', 'search_route_stop'),		

		)
