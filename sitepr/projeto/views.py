from datetime import datetime

from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Evento, Organizacao
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your views here.

#PAGINA INICIAL
def index(request):
    return render(request, 'projeto/index.html')

def month_names(month):
    switcher = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    return switcher.get(month)


#PAGINA EVENTOS
def eventos(request):
    month = datetime.now().month
    current_month = month_names(month)
    next_month = month_names(month + 1)
    next_next_month = month_names(month + 2)
    current_month_list = Evento.objects.filter(data__month=month)
    next_month_list = Evento.objects.filter(data__month=month + 1)
    next_next_month_list = Evento.objects.filter(data__month=month + 2)
    context = {'current_month_list': current_month_list, 'next_month_list': next_month_list, 'next_next_month_list': next_next_month_list, 'current_month': current_month, 'next_month':next_month, 'next_next_month':next_next_month}
    return render(request, 'projeto/eventos.html',context)

#CRIAR EVENTO
def criar_evento(request):
    if request.method == "POST":
        u = request.user
        org = u.organizacao
        new_evento = Evento()
        new_evento.nome = request.POST['nome_evento']
        new_evento.descricao = request.POST['descricao_evento']
        new_evento.local = request.POST['local']
        new_evento.data = request.POST['data']
        new_evento.organizacao = org
        new_evento.save()
        return HttpResponseRedirect(reverse('projeto:eventos', ))
    else:
        return render(request, 'projeto/criar_evento.html')



#ABRIR OS DETALHES DE UM EVENTO
def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'projeto/detalhe_evento.html', {'evento': evento})

#PAGINA MEUS EVENTOS
def meus_eventos(request):
    eventos_list = Evento.objects.filter(organizacao=request.user.organizacao)
    context = {'eventos_list': eventos_list}
    return render(request, 'projeto/meus_eventos.html',context)

def detalhe_meus_eventos(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'projeto/apagar_evento.html',{'evento': evento})

def apagar_evento(request,evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.delete()
    return render(request, 'projeto/meus_eventos.html')

#PAGINA SOBRE NOS
def sobrenos(request):
    return render(request, 'projeto/sobre_nos.html')

#PAGINA PARCEIROS
def parceiros(request):
    org_list = Organizacao.objects.all()
    context = {'org_list': org_list}
    return render(request, 'projeto/parceiros.html', context)

#PAGINA LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # direccionar para página de sucesso
            return render(request, 'projeto/index.html')
        else:
            # direccionar para página de insucesso
            return render(request, 'projeto/login.html', {'error_message': "Utilizador não existe"})
    else:
        return render(request, 'projeto/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'projeto/index.html')

#PAGINA REGISTAR
def registo(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
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
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return HttpResponseRedirect(reverse('projeto:index', ))
    else:
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




def registar_org(request):
    if request.method == 'POST':
        name_org = request.POST['name_org']
        bio = request.POST['bio']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if username_exists(username):
            return render(request, 'projeto/registar_organizacao.html', {'error_message': "Este utilizador já está registado"})
        elif email_exists(email):
            return render(request, 'projeto/registar_organizacao.html', {'error_message': "Este utilizador já está registado"})
        elif password != confirm_password:
            return render(request, 'projeto/registar_organizacao.html', {'error_message': "As passwords não coincidem"})
        else:
            user = User.objects.create_user(username,email,password)
            org = Organizacao(user=user, nome=name_org, descricao=bio,)
            org.save()
            user.save()
        return HttpResponseRedirect(reverse('projeto:user_login', ))
    else:
        return render(request, 'projeto/registar_organizacao.html')


def profile(request):
    return render(request, 'projeto/profile.html',)


def img_upload(request):
 if request.method == 'POST' and request.FILES['myfile']:
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    return render(request, 'projeto/img_upload.html', {'uploaded_file_url': uploaded_file_url})
 return render(request, 'projeto/img_upload.html')





