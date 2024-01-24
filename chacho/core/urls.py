from django.urls import path
from .views import home, formulario, lista_juegos, comando, lista_comandos, videos, upload_excel, speedtest
from .views import custom_logout
urlpatterns = [
    path('home', home, name="home"),
    path('formulario/', formulario, name="formulario"),
    path('', lista_juegos, name='lista_juegos'),
    path('comando/', comando, name="comando"),
    path('lista_comandos', lista_comandos, name="lista_comandos"),
    path('videos', videos, name="videos"),
    path('upload_excel/', upload_excel, name='upload_excel'),
    path('speedtest', speedtest, name="speedtest"),
    path('logout/', custom_logout, name='logout'),
]