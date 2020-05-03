from django.urls import path, re_path

from device import views

app_name = "device"

urlpatterns = [
    path("ipinfo/api/", views.ipInfo, name = "ipInfo"),

    path('', views.device, name = "deviceRoot"),
]
