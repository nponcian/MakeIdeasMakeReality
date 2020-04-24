from django.urls import path, re_path

from home import views

app_name = 'home'

urlpatterns = [
    re_path('^home/?$', views.home, name = "home"),
    re_path('^index/?$', views.home, name = "index"),
    path('', views.home, name = "homeRoot"),

    re_path('^.*$', views.notFound, name = "notFound"),
]
