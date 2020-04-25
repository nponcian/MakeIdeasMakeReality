from django.urls import path, re_path

from text import views

app_name = 'text'

urlpatterns = [
    path('formattab/', views.formatTab, name = "formatTab"),
    path('generatepassword/', views.generatePassword, name = "generatePassword"),
    path('', views.text, name = "textRoot"),
]
