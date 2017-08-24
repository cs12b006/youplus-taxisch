from django.shortcuts import render, render_to_response, redirect
from .models import Driver
from rest_framework import serializers, viewsets
from dashboard.models import Request
from datetime import datetime, timezone
from django.http import JsonResponse
from time import sleep
from threading import Thread

class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['id']

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

def driver_view(request, driver_id):
    d = Driver.objects.filter(pk=driver_id).first()
    if not d:
        response = render_to_response('404.html')
        return response

    return render(request, 'driver-home.html', {"did": driver_id})

# takes datetime object gives min,sec ago from now
def get_time_from_now(ti):
    if ti is None:
        return None, None
    t_diff = (datetime.now(timezone.utc)-ti).total_seconds()
    return int(t_diff/60), int(t_diff%60)

def waiting_requests(request, driver_id):
    rs = Request.objects.filter(picked_by=None, status = 0)
    a = []
    for r in rs:
        t_diff = get_time_from_now(r.req_time)
        a.append({"rid": r.pk, "cid": r.raised_by.pk, "tmin": t_diff[0], "tsec": t_diff[1]})
    return render(request, 'waiting-snippet.html', {"a": a, "did": driver_id})

def ongoing_driver(request, driver_id):
    rs = Request.objects.filter(picked_by=driver_id, status=1).first()
    a = []
    if rs is not None:
        req_t = get_time_from_now(rs.req_time)
        pick_t = get_time_from_now(rs.picked_time)
        a.append({"rid": rs.pk, "cid": rs.raised_by.pk, "rtmin": req_t[0], "rtsec": req_t[1],
            "ptmin": pick_t[0], "ptsec": pick_t[1]})
    return render(request, 'driver-snippet.html', {"a": a})

def completed_driver_req(request, driver_id):
    r = Request.objects.filter(picked_by=driver_id, status=2)
    a = []
    for rs in r:
        req_t = get_time_from_now(rs.req_time)
        pick_t = get_time_from_now(rs.complete_time)
        comp_t = get_time_from_now(rs.picked_time)
        a.append({"rid": rs.pk, "cid": rs.raised_by.pk, "rtmin": req_t[0], "rtsec": req_t[1],
            "ptmin": pick_t[0], "ptsec": pick_t[1], "ctmin": comp_t[0], "ctsec": comp_t[1]})
    return render(request, 'driver-snippet.html', {"a": a})

# changes the ride to completed after 5 mins
def complete_ride(r_id):
    sleep(5*60)
    r = Request.objects.filter(pk=r_id).first()
    r.status = 2
    r.complete_time = datetime.now(timezone.utc)
    r.save()

def select_req(request):
    if request.method == "POST":
        d, req = request.POST.get("d",None), request.POST.get("r",None)
        if d is None or req is None:
            return JsonResponse({'success':False})
        rs = Request.objects.filter(pk=req).first()
        driver = Driver.objects.filter(pk=d).first()
        if rs is None or driver is None:
            return JsonResponse({'success':False})
        if rs.picked_by is not None:
            return JsonResponse({'success':True, 'picked': True})
        rs.picked_by = driver
        rs.status = 1
        rs.picked_time = datetime.now(timezone.utc)
        #simulate ride ending 5 min from now
        thread2 = Thread(target = complete_ride, args = (req, ))
        thread2.start()
        rs.save()
        return JsonResponse({'success':True, 'picked': False})
    return JsonResponse({'success':False})
