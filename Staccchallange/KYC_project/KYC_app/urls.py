from django.urls import path
from . import views


urlpatterns = [
    path('PEP_check', views.PEP_check, name="home"),
]
