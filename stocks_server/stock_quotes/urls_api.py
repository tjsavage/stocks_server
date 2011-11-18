from django.conf.urls import patterns, include, url

urlpatterns = patterns('stock_quotes.views_api',
    url(r'^(?P<symbol>\w+)/$', 'index'),
    url(r'^(?P<symbol>\w+)/current_price/$', 'current_price'),
)