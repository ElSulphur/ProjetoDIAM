from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'projeto'
urlpatterns = [
 #index
 path("", views.index, name="index"),
 path("eventos" , views.eventos, name="eventos"),
 path("sobrenos" , views.sobrenos, name="sobrenos"),
 path("parceiros" , views.parceiros, name="parceiros"),
 path("user_login" , views.user_login, name="user_login"),
 path("registo" , views.registo, name="registo"),
 path("meus_eventos" , views.meus_eventos, name="meus_eventos"),
 path("meus_eventos/detalhe_meus_eventos/<int:evento_id>" , views.detalhe_meus_eventos, name="detalhe_meus_eventos"),
 path("meus_eventos/apagar_evento/<int:evento_id>", views.apagar_evento, name="apagar_evento"),
 path("eventos/criar_evento" , views.criar_evento, name="criar_evento"),
 path("registo/registar_org" , views.registar_org, name="registar_org"),
 path("eventos/<int:evento_id>" , views.detalhe_evento, name="detalhe_evento"),
 path("profile" , views.profile, name="profile"),
 path("logout" , views.logout_view, name="logout_view"),
 path('img_upload', views.img_upload, name='img_upload'),

]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)