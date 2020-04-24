from django.urls import include, path, re_path

from service import views

app_name = 'service'

urlpatterns = [
    path('text/', include('text.urls', namespace = 'text')),
    path('', views.service, name = "serviceRoot"),
]
