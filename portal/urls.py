from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^cadastre_seu_imovel/$', views.cadastre_seu_imovel),
]