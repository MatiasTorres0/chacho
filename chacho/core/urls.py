from django.urls import path
from .views import home, formulario, crear_jugador, lista_juegos, comando, lista_comandos, videos, upload_excel, speedtest, ticket_list, ticket_detail, create_ticket
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
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/<int:ticket_id>/', ticket_detail, name='ticket_detail'),
    path('tickets/create/', create_ticket, name='create_ticket'),
    path('equipo', crear_jugador, name='equipo'),
]