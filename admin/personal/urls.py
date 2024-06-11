from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('form/', views.formulario, name="formulario"),
    path('list', views.listado, name="listado"),
]