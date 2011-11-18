from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stocks_server.views.home', name='home'),
    # url(r'^stocks_server/', include('stocks_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^api/portfolio/', include('portfolio.urls_api')),
    url(r'^api/logs/', include('portfolio_logs.urls_api')),
    url(r'^api/stock_quotes/', include('stock_quotes.urls_api')),
)

urlpatterns += staticfiles_urlpatterns()
