from django.conf.urls import patterns, include, url 

from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^$', 'test'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<slug>\w+)/$', test),
    url(r'^ask/', test),
    url(r'^popular/', test),
    url(r'^new/', test)
)
