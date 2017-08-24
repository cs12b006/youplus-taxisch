from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^waiting/(?P<driver_id>[0-9]+)/$', views.waiting_requests, name='waiting_requests'),
    url(r'^ongoing/(?P<driver_id>[0-9]+)/$', views.ongoing_driver, name='ongoing_driver'),
    url(r'^completed/(?P<driver_id>[0-9]+)/$', views.completed_driver_req, name='completed_driver_req'),
    url(r'^selected/$', views.select_req, name='select_req')
]
