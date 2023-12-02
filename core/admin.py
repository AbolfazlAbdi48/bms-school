from django.contrib import admin
from .models import Sensor, SensorDetail, Lamp, UserToken

# Register your models here.
admin.site.register(Sensor)
admin.site.register(SensorDetail)
admin.site.register(Lamp)
admin.site.register(UserToken)
