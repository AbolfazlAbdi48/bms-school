import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView

from core.models import Sensor, Lamp, SensorDetail


# Create your views here.
@login_required
def home_view(request):
    sensors = Sensor.objects.filter(user=request.user)
    lamps = Lamp.objects.filter(user=request.user)

    context = {
        "sensors": sensors,
        "lamps": lamps
    }
    return render(request, 'core/home.html', context)


class LampDetailView(LoginRequiredMixin, DetailView):
    model = Lamp
    template_name = 'core/lamp_detail.html'


class SensorDetailView(LoginRequiredMixin, DetailView):
    model = Sensor
    template_name = 'core/sensor_detail.html'


@login_required
@csrf_exempt
def create_sensor_detail_view(request, sensor_id):
    if request.method == "POST":
        json_data = json.loads(request.body)
        value = json_data["value"]
        try:
            token = json_data["token"]
            sensor = get_object_or_404(Sensor, id=sensor_id, user__usertoken__token=token)
            sensor_detail = SensorDetail.objects.create(
                sensor=sensor,
                value=value[1],
            )
            return JsonResponse({"status": "OK", "token": token})
        except:
            return JsonResponse({"status": "NOT VALID"})


@login_required
@csrf_exempt
def update_lamp_status_view(request, lamp_id, token):
    lamp = get_object_or_404(Lamp, id=lamp_id, user__usertoken__token=token)

    if lamp.status == "0":
        lamp.status = "1"
        messages.success(request, f"وضعیت {lamp.name} به ON تغییر پیدا کرد")
    else:
        lamp.status = "0"
        messages.success(request, f"وضعیت {lamp.name} به OFF تغییر پیدا کرد")
    lamp.save()

    if request.method == "POST":
        return JsonResponse({"status": lamp.get_status_display(), "token": token})
    return redirect("lamp-detail", pk=lamp_id)


@login_required
@csrf_exempt
def get_lamp_statu_view(request, lamp_id, token):
    lamp = get_object_or_404(Lamp, id=lamp_id, user__usertoken__token=token)
    return JsonResponse({"status": lamp.get_status_display(), "token": token})


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    success_message = "حساب کاربری با موفقیت ساخته شد، لطفا وارد حساب شوید."
