#url.py
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'ankiety.ank.views.index'),
    url(r'^detail/(?P<poll_id>\d+)/$', 'ankiety.ank.views.detail'),

)
