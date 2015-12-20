from django.shortcuts import render
from django.utils import timezone
from .models import Imovel

def home(request):
    imoveis = Imovel.objects.filter(data_divulgacao__lte=timezone.now()).order_by('data_divulgacao')
    return render(request, 'portal/index.html', {'imoveis': imoveis})

def cadastre_seu_imovel(request):
    return render(request, 'portal/cadastre-seu-imovel.html', {})