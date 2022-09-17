from django.urls import path
from . import views


urlpatterns = [
    path('', views.PEP, name='PEP'),
    path('PEP/', views.PEP, name="PEP"),
    path('roller/', views.roller, name="roller"),
    path('enheter/', views.enheter, name="enheter"),
]
