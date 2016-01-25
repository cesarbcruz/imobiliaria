from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^cadastre_seu_imovel/$', views.cadastre_seu_imovel),
    url(r'^documentos/$', views.documentos),
    url(r'^simule_seu_financiamento/$', views.simule_seu_financiamento),
    url(r'^contatos/$', views.contatos),
    url(r'^pesquisar/$', views.pesquisar),
    url(r'^pesquisar_por_codigo/$', views.pesquisar_por_codigo),
    url(r'^detalhes_imovel/(?P<pk>[0-9]+)/$', views.detalhes_imovel),
]