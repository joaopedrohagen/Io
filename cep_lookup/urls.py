from django.urls import path
from .views import buscar_cep
from . import views

urlpatterns = [
    path('buscar_cep/<str:cep>/', views.buscar_cep, name='buscar_cep'),
]
