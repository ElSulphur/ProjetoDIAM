from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Evento
# Create your views here.

#PAGINA PRINCIPAL
def index(request):
    return render(request, 'projeto/index.html')

def eventos(request):
    return render(request, 'projeto/eventos.html')

def criar_evento(request):
    return render(request, 'projeto/criar_evento.html')

def guardar_evento(request):
    new_evento = Evento()
    new_evento.nome = request.POST['nome_evento']
    new_evento.descricao = request.POST['descricao_evento']
    new_evento.local = request.POST['local']
    new_evento.data = request.POST['data']
    new_evento.save()
    return HttpResponseRedirect(reverse('projeto:eventos',))

def sobrenos(request):
    return render(request, 'projeto/sobre_nos.html')

def parceiros(request):
    return render(request, 'projeto/parceiros.html')

def login(request):
    return render(request, 'projeto/login.html')

def registo(request):
    return render(request, 'projeto/registo.html')




