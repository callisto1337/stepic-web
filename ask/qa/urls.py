from django.conf.urls import patterns, include, url 

from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^$', 'test'),
    url(r'^login/', test)
)
