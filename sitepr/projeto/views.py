from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Evento
from django.contrib.auth import authenticate
# Create your views here.

#PAGINA INICIAL
def index(request):
    return render(request, 'projeto/index.html')

#PAGINA EVENTOS
def eventos(request):
    latest_question_list = Evento.objects.order_by('data')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'projeto/eventos.html',context)

#BOTAO CRIAR EVENTO
def criar_evento(request):
    return render(request, 'projeto/criar_evento.html')

#GUARDAR UM EVENTO
def guardar_evento(request):
    new_evento = Evento()
    new_evento.nome = request.POST['nome_evento']
    new_evento.descricao = request.POST['descricao_evento']
    new_evento.local = request.POST['local']
    new_evento.data = request.POST['data']
    new_evento.save()
    return HttpResponseRedirect(reverse('projeto:eventos',))

#ABRIR OS DETALHES DE UM EVENTO
def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'projeto/detalhe_evento.html', {'evento': evento})

#PAGINA SOBRE NOS
def sobrenos(request):
    return render(request, 'projeto/sobre_nos.html')

#PAGINA PARCEIROS
def parceiros(request):
    return render(request, 'projeto/parceiros.html')

#PAGINA LOGIN
def login(request):
    return render(request, 'projeto/login.html')

#PAGINA REGISTAR
def registo(request):
    return render(request, 'projeto/registo.html')

#validar se um username já existe
def username_exists(username):
    if User.objects.filter(username=username).exists():
        return True

    return False

#validar se um email já existe
def email_exists(email):
    if User.objects.filter(email=email).exists():
        return True

    return False

#GUARDAR UM REGISTO = NOVO UTILIZADOR
def registar(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if username_exists(username):
        return render(request, 'projeto/registo.html', {'error_message': "Este utilizador já está registado"})
    elif email_exists(email):
        return render(request, 'projeto/registo.html', {'error_message': "Este utilizador já está registado"})
    elif password != confirm_password:
        return render(request, 'projeto/registo.html', {'error_message': "As passwords não coincidem"})
    else:
        user = User.objects.create_user(username,email,password)
        user.save()
    return HttpResponseRedirect(reverse('projeto:index', ))







