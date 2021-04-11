from django.urls import include, path
from . import views
# (. significa que importa views da mesma directoria)

app_name = 'votacao'
urlpatterns = [
# ex: votacao/
 path("", views.index, name='index'),
 # ex: votacao/1
 path('<int:questao_id>', views.detalhe, name='detalhe'),
 # ex: votacao/3/resultados
 path('<int:questao_id>/resultados', views.resultados, name='resultados'),
 # ex: votacao/5/voto
 path('<int:questao_id>/voto', views.voto, name='voto'),
# ex: votacao/novaquestao
 path("gravarquestao", views.gravarquestao, name='gravarquestao'),

 path("novaquestao", views.novaquestao, name='novaquestao'),

 path("<int:questao_id>/novaopcao", views.novaopcao, name='novaopcao'),

 path("<int:questao_id>/gravaropcao", views.gravaropcao, name='gravaropcao'),

 path("listarquestao", views.listarquestao, name='listarquestao'),

 path("apagarquestao", views.apagarquestao, name='apagarquestao'),

 path("<int:questao_id>/listaropcao", views.listaropcao, name='listaropcao'),

 path("<int:questao_id>/apagaropcao", views.apagaropcao, name='apagaropcao'),
]
