import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from core.models import Sensor, Lamp, SensorDetail


# Create your views here.

def home_view(request):
    sensors = Sensor.objects.all()
    lamps = Lamp.objects.all()

    context = {
        "sensors": sensors,
        "lamps": lamps
    }
    return render(request, 'core/home.html', context)


class LampDetailView(DetailView):
    model = Lamp
    template_name = 'core/lamp_detail.html'


class SensorDetailView(DetailView):
    model = Sensor
    template_name = 'core/sensor_detail.html'


@csrf_exempt
def create_sensor_detail_view(request, sensor_id):
    if request.method == "POST":
        value = request.body.decode('utf-8').split('=')
        sensor_detail = SensorDetail.objects.create(sensor_id=sensor_id, value=value[1])

        return HttpResponse({"status": "OK"})


@csrf_exempt
def update_lamp_status_view(request, lamp_id):
    lamp = get_object_or_404(Lamp, id=lamp_id)

    if lamp.status == "0":
        lamp.status = "1"
        messages.success(request, f"وضعیت {lamp.name} به ON تغییر پیدا کرد")
    else:
        lamp.status = "0"
        messages.success(request, f"وضعیت {lamp.name} به OFF تغییر پیدا کرد")
    lamp.save()

    if request.method == "POST":
        return HttpResponse({lamp.status: "OK"})
    return redirect("lamp-detail", pk=lamp_id)
