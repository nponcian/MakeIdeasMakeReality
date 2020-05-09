from django.urls import path, re_path

from text import views

app_name = 'text'

urlpatterns = [
    path('ciphermessage/', views.cipherMessage, name = "cipherMessage"),
    path('countword/', views.countWord, name = "countWord"),
    path('formattabindent/', views.formatTabIndent, name = "formatTabIndent"),
    path('generatecode/', views.generateCode, name = "generateCode"),
    path('limitlinelength/', views.limitLineLength, name = "limitLineLength"),
    path('', views.text, name = "textRoot"),
]
