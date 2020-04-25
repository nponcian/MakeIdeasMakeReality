from django.urls import path, re_path

from text import views

app_name = 'text'

urlpatterns = [
    path('ciphermessage/', views.cipherMessage, name = "cipherMessage"),
    path('formattabindent/', views.formatTabIndent, name = "formatTabIndent"),
    path('generatepassword/', views.generatePassword, name = "generatePassword"),
    path('', views.text, name = "textRoot"),
]
