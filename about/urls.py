from django.urls import include, path, re_path

from about import views

app_name = 'about'

urlpatterns = [
    path('whoami/', views.whoAmI, name = "whoAmI"),

    re_path('^(mimr/)?$', views.aboutMimr, name = "aboutMimr"),
]
