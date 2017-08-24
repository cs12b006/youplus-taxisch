from django.shortcuts import render
from .models import Request
from driverapp.views import get_time_from_now
from .serializers import RequestSerializer
from rest_framework import viewsets

class ReqViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-picked_time', '-req_time')
    serializer_class = RequestSerializer

# Create your views here.
# Insert Request object instance given customer
def request_by_customer(customer):
    r = Request.objects.create(raised_by=customer)

def full_view(request):
    return render(request, 'dashboard.html', {})

def get_requests_for_dashboard(request):
    a = []
    rs = Request.objects.order_by('-picked_time', '-req_time')
    for r in rs:
        st = {0:"Waiting", 1:"Ongoing", 2: "Complete"}
        st_time = {0:"req_time", 1:"picked_time", 2: "complete_time"}
        st_v, st_t = "", [0,0]
        if r.status in st:
            st_v = st[r.status]
            attr_val = st_time[r.status]
            st_t = get_time_from_now(getattr(r, attr_val))
        cid = getattr(r.raised_by, 'id', None)
        did = getattr(r.picked_by, 'id', None)
        a.append({"cid":cid, "rid":r.pk, "tmin":st_t[0],"tsec":st_t[1], "driver":did, "stat": st_v})
    return render(request, 'dashboard-entries.html', {"a": a})
