from django.urls import path, re_path

from text import views

app_name = 'text'

urlpatterns = [
    path('ciphermessage/', views.cipherMessage, name = "cipherMessage"),
    path('ciphermessage/api/', views.CipherMessageApi.as_view(), name = "CipherMessageApi"),
    path('commonword/', views.commonWord, name = "commonWord"),
    path('commonword/api/', views.CommonWordApi.as_view(), name = "CommonWordApi"),
    path('formattabindent/', views.formatTabIndent, name = "formatTabIndent"),
    path('formattabindent/api/', views.FormatTabIndentApi.as_view(), name = "FormatTabIndentApi"),
    path('generatecode/', views.generateCode, name = "generateCode"),
    path('generatecode/api/', views.GenerateCodeApi.as_view(), name = "GenerateCodeApi"),
    path('limitlinelength/', views.limitLineLength, name = "limitLineLength"),
    path('limitlinelength/api/', views.LimitLineLengthApi.as_view(), name = "LimitLineLengthApi"),
    path('', views.text, name = "textRoot"),
]
