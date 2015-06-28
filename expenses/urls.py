__author__ = 'wfournier'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.month_detail, name='month'),
    url(r'^(?P<month>[0-9]+)/withdrawal/(?P<pk>-?[0-9]+)/$', views.add_or_update_withdrawal, name='withdrawal'),
    url(r'^(?P<month>[0-9]+)/withdrawal/(?P<pk>-?[0-9]+)/delete$', views.delete_withdrawal, name='withdrawal-delete'),
    url(r'^(?P<month>[0-9]+)/deposit/(?P<pk>-?[0-9]+)/$', views.add_or_update_deposit, name='deposit'),
    url(r'^(?P<month>[0-9]+)/deposit/(?P<pk>-?[0-9]+)/delete$', views.delete_deposit, name='deposit-delete'),
]