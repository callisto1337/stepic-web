rom django.conf.urls import patterns, include, url
                                                                                
from django.contrib import admin admin.autodiscover()
                                                                                
urlpatterns = [
    # Examples: url(r'^$', 'ask.views.home', name='home'), 
    # url(r'^blog/', include('blog.urls')),
                                                                                
    url(r'^', 'qa.views.test', name='test')),
                                                                                
    url(r'^admin/', include(admin.site.urls)), 
]
                                                                                
                                                                                
                      
