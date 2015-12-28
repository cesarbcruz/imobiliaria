from django.shortcuts import render
from django.utils import timezone
from .models import Destaque
from django.core.mail import send_mail

def home(request):
    destaques = Destaque.objects.filter(data_inicio_divulgacao__lte=timezone.now(), data_final_divulgacao__gte=timezone.now()).order_by('data_inicio_divulgacao')
    return render(request, 'portal/index.html', {'destaques': destaques})

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


