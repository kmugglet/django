from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /elpheba/
    url(r'^$', views.index, name='index'),
    # ex: /elpheba/odb?sjdkskdsad
    url(r'^odb/(?P<payload>.*)', views.odb, name='odb'),
    # ex: /elpheba/5/
    url(r'^(?P<acct>[0-9]+)/$', views.check),
    # ex: /elpheba/5/start/
    url(r'^(?P<acct>[0-9]+)/start/$', views.start),
    # ex: /elpheba/5/completed/123456
    url(r'^(?P<acct>[0-9]+)/completed/(?P<intEquity>[0-9]+)$', views.completed),
    # ex: /elpheba/5/withdrawl/123456/1234
    url(r'^(?P<acct>[0-9]+)/withdrawl/(?P<intEquity>[0-9]+)/(?P<intWithdrawl>[0-9\-]+)$', views.withdrawl),
    # ex: /elpheba/5/transfer/123456789/1234/987654321
    url(r'^(?P<fromAcct>[0-9]+)/transfer/(?P<amount>[0-9\-]+)/(?P<toAcct>[0-9]+)/$', views.transfer),
    # ex: /elpheba/5/newOrders
    url(r'^(?P<fromAcct>[0-9]+)/newOrders$', views.newOrders),


]
