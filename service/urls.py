from django.urls import include, path, re_path

from home import views

app_name = 'service'

urlpatterns = [
    path('text/', include('text.urls', namespace = 'text')),
]
