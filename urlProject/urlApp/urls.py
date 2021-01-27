from django.conf.urls import url
from urlApp import views

urlpatterns = [
    url(r'^firstapp/', views.firstappinfo),
    url(r'^secondapp/', views.secondappinfo),
    url(r'^thirdapp/', views.thirdappinfo),
    url(r'^fourthapp/', views.fourthappinfo),
]
