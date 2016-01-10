#coding: utf-8
from django.shortcuts import render
from django.utils import timezone
from .models import Destaque, Bairro, TipoImovel, TIPONEGOCIACAO
from django.core.mail import send_mail
from portal.models import Imovel


def home(request):
    bairros = Bairro.objects.all();
    tipoimovel = TipoImovel.objects.all();
    destaqueslocacao = Destaque.objects.filter(imovel__tipo_negociacao='0', data_inicio_divulgacao__lte=timezone.now(), data_final_divulgacao__gte=timezone.now()).order_by('data_inicio_divulgacao')
    destaquesvenda = Destaque.objects.filter(imovel__tipo_negociacao='1', data_inicio_divulgacao__lte=timezone.now(), data_final_divulgacao__gte=timezone.now()).order_by('data_inicio_divulgacao')
    return render(request, 'portal/index.html', {'destaqueslocacao': destaqueslocacao, 'destaquesvenda' : destaquesvenda, 'bairros' : bairros, 'tipoimovel' : tipoimovel})

def persquisar(request):
    bairros = Bairro.objects.all();
    tipoimovel = TipoImovel.objects.all();
    if request.method == 'POST':
        tipo_negocio = request.POST.get("tipo_negocio", "")
        tipo_imovel = request.POST.get("tipo_imovel", "")
        valor_maximo = request.POST.get("valor_maximo", "")
        bairro = request.POST.get("bairro", "")
        imoveis = None
        if tipo_negocio and tipo_imovel:

            descricao_tipo_negocio = None
            if tipo_negocio == '0':
                descricao_tipo_negocio = 'Alugar Imóvel'
            elif tipo_negocio == '1':
                descricao_tipo_negocio = 'Comprar Imóvel'


            descricao_tipo_imovel = TipoImovel.objects.get(pk=tipo_imovel).descricao

            imoveis = Imovel.objects.filter(tipo_negociacao = tipo_negocio,tipo__id = tipo_imovel, data_divulgacao__lte=timezone.now()).order_by('id')
            if valor_maximo:
               if tipo_negocio == '0':
                    if valor_maximo == '1':
                        imoveis = imoveis.filter(valor__lte=500.0)
                    elif valor_maximo == '2':
                        imoveis = imoveis.filter(valor__gte=500.0, valor__lte=1000.0)
                    elif valor_maximo == '3':
                        imoveis = imoveis.filter(valor__gte=1000.0, valor__lte=1500.0)
                    elif valor_maximo == '4':
                        imoveis = imoveis.filter(valor__gte=1500.0, valor__lte=2000.0)
                    elif valor_maximo == '5':
                        imoveis = imoveis.filter(valor__gte=2000.0, valor__lte=3000.0)
                    elif valor_maximo == '6':
                        imoveis = imoveis.filter(valor__gte=3000.0, valor__lte=4000.0)
                    elif valor_maximo == '7':
                        imoveis = imoveis.filter(valor__gte=4000.0, valor__lte=6000.0)
                    elif valor_maximo == '8':
                        imoveis = imoveis.filter(valor__gte=10000.0)
               else:
                    if valor_maximo == '1':
                        imoveis = imoveis.filter(valor__lte=100000.0)
                    elif valor_maximo == '2':
                        imoveis = imoveis.filter(valor__gte=100000.0, valor__lte=150000.0)
                    elif valor_maximo == '3':
                        imoveis = imoveis.filter(valor__gte=150000.0, valor__lte=200000.0)
                    elif valor_maximo == '4':
                        imoveis = imoveis.filter(valor__gte=200000.0, valor__lte=250000.0)
                    elif valor_maximo == '5':
                        imoveis = imoveis.filter(valor__gte=250000.0, valor__lte=300000.0)
                    elif valor_maximo == '6':
                        imoveis = imoveis.filter(valor__gte=300000.0, valor__lte=400000.0)
                    elif valor_maximo == '7':
                        imoveis = imoveis.filter(valor__gte=400000.0, valor__lte=600000.0)
                    elif valor_maximo == '8':
                        imoveis = imoveis.filter(valor__gte=600000.0)

            if bairro:
                imoveis = imoveis.filter(bairro_id=bairro)

            return render(request, 'portal/pesquisar.html', {'imoveis' : imoveis, 'bairros' : bairros, 'tipoimovel': tipoimovel, 'mensagem' : '', 'descricao_tipo_negocio':descricao_tipo_negocio, 'descricao_tipo_imovel' : descricao_tipo_imovel})
        else:
            return render(request, 'portal/pesquisar.html', {'imoveis' : imoveis, 'bairros' : bairros, 'tipoimovel': tipoimovel, 'mensagem' : 'Selecione o Tipo de Negócio e o Tipo do Imóvel !', 'descricao_tipo_negocio':'', 'descricao_tipo_imovel' : ''})
    else:
        return render(request, 'portal/pesquisar.html', {'bairros' : bairros, 'tipoimovel': tipoimovel, 'mensagem' : '', 'descricao_tipo_negocio':'', 'descricao_tipo_imovel' : ''})


def cadastre_seu_imovel(request):
    return render(request, 'portal/cadastre-seu-imovel.html', {})

def documentos(request):
    return render(request, 'portal/documentos.html', {})

def simule_seu_financiamento(request):
    return render(request, 'portal/simule-seu-financiamento.html', {})

def contatos(request):
    if request.method == 'GET':
        return render(request, 'portal/contatos.html', {'mensagem':"Preencha todos os campos e selecione Enviar"})
    elif request.method == 'POST':
        nome = request.POST.get("custom_U766", "")
        email = request.POST.get("Email", "")
        mensagem = request.POST.get("custom_U772", "")

        #toaddrs = "atendimento@corretaimov.com.br"
        #fromaddr = "atendimento@corretaimov.com.br"
        toaddrs = "cesar.analista@gmail.com"
        fromaddr = "cesar.analista@gmail.com"

        msg="Nome: "+nome+"\n"
        msg+="Email: "+email+"\n"
        msg+="Mensagem: "+mensagem+"\n"
        print(msg)

        try:
            send_mail('Contato do Site', msg, fromaddr, [toaddrs], fail_silently=False)
        except:
            return render(request, 'portal/contatos.html', {'mensagem':"Falha ao enviar mensagem, tente mais tarde!"})

        return render(request, 'portal/contatos.html', {'mensagem':"Mensagem enviada com sucesso!"})

def detalhes_imovel(request, pk):
    imovel = None;
    if pk:
        imovel = Imovel.objects.get(pk=pk)

    return render(request, 'portal/detalhesimovel.html', {'imovel': imovel})
