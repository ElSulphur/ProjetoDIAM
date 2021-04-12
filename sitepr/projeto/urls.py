from django.urls import include, path
from . import views

app_name = 'projeto'
urlpatterns = [
 #index
 path("", views.index, name="index"),
 path("eventos" , views.eventos, name="eventos"),
 path("sobrenos" , views.sobrenos, name="sobrenos"),
 path("parceiros" , views.parceiros, name="parceiros"),
 path("login" , views.login, name="login"),
 path("registo" , views.registo, name="registo"),
 path("eventos/criar_evento" , views.criar_evento, name="criar_evento"),
 path("guardar_evento" , views.guardar_evento, name="guardar_evento"),
 path("registar" , views.registar, name="registar"),
 path("eventos/<int:evento_id>" , views.detalhe_evento, name="detalhe_evento"),
]