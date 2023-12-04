"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from core.views import (
    home_view,
    LampDetailView,
    SensorDetailView,
    create_sensor_detail_view,
    update_lamp_status_view,
    get_lamp_statu_view,
    SignUpView,
    SensorCreateView,
    LampCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view()),
    path('', home_view, name='home'),
    path('lamp/create', LampCreateView.as_view(), name='lamp-create'),
    path('sensor/create', SensorCreateView.as_view(), name='sensor-create'),
    path('lamp/<int:pk>', LampDetailView.as_view(), name='lamp-detail'),
    path('sensor/<int:pk>', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensor/<sensor_id>/create', create_sensor_detail_view, name='sensor-detail-create'),
    path('lamp/<lamp_id>/update/<token>', update_lamp_status_view, name='lamp-detail-update'),
    path('lamp/<lamp_id>/status/<token>', get_lamp_statu_view, name='lamp-detail-status'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
