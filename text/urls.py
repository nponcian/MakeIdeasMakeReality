from django.urls import path, re_path

from text import views

app_name = 'text'

# Note: APPEND_SLASH doesn't work for HTTP POST, so it is important to use /? for the APIs

urlpatterns = [
    path('ciphermessage/', views.cipherMessage, name = "cipherMessage"),
    re_path(r'ciphermessage/api/?', views.CipherMessageApi.as_view(), name = "CipherMessageApi"),
    path('commonword/', views.commonWord, name = "commonWord"),
    re_path(r'commonword/api/?', views.CommonWordApi.as_view(), name = "CommonWordApi"),
    path('formattabindent/', views.formatTabIndent, name = "formatTabIndent"),
    re_path(r'formattabindent/api/?', views.FormatTabIndentApi.as_view(), name = "FormatTabIndentApi"),
    path('generatecode/', views.generateCode, name = "generateCode"),
    re_path(r'generatecode/api/?', views.GenerateCodeApi.as_view(), name = "GenerateCodeApi"),
    path('wrapline/', views.wrapLine, name = "wrapLine"),
    re_path(r'wrapline/api/?', views.WrapLineApi.as_view(), name = "WrapLineApi"),
    path('', views.text, name = "textRoot"),
]
