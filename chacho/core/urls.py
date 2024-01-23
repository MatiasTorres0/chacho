from django.urls import path
from .views import home, formulario, lista_juegos, comando, lista_comandos

urlpatterns = [
    path('', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('lista_juegos/', lista_juegos, name='lista_juegos'),
    path('comando/', comando, name="comando"),
    path('lista_comandos', lista_comandos, name="lista_comandos"),
]