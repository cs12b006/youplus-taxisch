"""taxiQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from customerapp.views import raise_request, CustViewSet
from dashboard.views import ReqViewSet
from driverapp.views import DriverViewSet, driver_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'requests', ReqViewSet)
router.register(r'customers', CustViewSet)
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^customerapp/', raise_request, name="customer_request"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^driver/', include('driverapp.urls')),
    url(r'^request/', include('dashboard.urls')),
    url(r'^driverapp/(?P<driver_id>[0-9]+)/$', driver_view, name="driver_view"),
]
