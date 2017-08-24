from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.full_view, name='full_view'),
    url(r'^selected/$', views.get_requests_for_dashboard, name='requests_for_dashboard')
]
