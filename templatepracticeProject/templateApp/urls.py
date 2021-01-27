from django.conf.urls import url
from templateApp import views

urlpatterns = [
    url(r'^lkottala/', views.praticewish),
]
