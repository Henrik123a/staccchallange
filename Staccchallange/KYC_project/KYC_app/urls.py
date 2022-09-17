from django.urls import path
from . import views


urlpatterns = [
    path('PEP', views.PEP, name="KYC"),
    path('roller', views.roller, name="KYC"),
    path('enheter', views.enheter, name="KYC"),

]
