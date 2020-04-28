from django.urls import path, re_path

from home import views

app_name = 'home'

urlpatterns = [
    path('api/ipinfo/', views.ipInfo, name = "ipInfo"),

    path('home/', views.home, name = "home"),
    path('', views.home, name = "homeRoot"),

    # re_path('^.*$', views.notFound, name = "notFound"), # this messes up with redirection from APPEND_SLASH = True
]
