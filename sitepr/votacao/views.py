#from django.shortcuts import render
#from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
#from .models import Questao
#from django.shortcuts import get_object_or_404, render
#from .models import Questao, Opcao
#from django.urls import reverse

from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .models import Questao, Opcao

# Create your views here.

def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    template = loader.get_template('votacao/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))
'''
def detalhe(request, questao_id):
    return HttpResponse("Esta e a questao %s." % questao_id)

def resultados(request, questao_id):
    response = "Estes sao os resultados da questao %s."
    return HttpResponse(response % questao_id)

def voto(request, questao_id):
    return HttpResponse("Votacao na questao %s." % questao_id)

def detalhe(request, questao_id):
 try:
    questao = Questao.objects.get(pk=questao_id)
 except Questao.DoesNotExist:
    raise Http404("A questao nao existe")
    return render(request, 'votacao/detalhe.html', {'questao': questao})
'''
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})

def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {
            'questao': questao,
            'error_message': "Não escolheu uma opção",
        })
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
        return HttpResponseRedirect( reverse('votacao:resultados', args=(questao.id,)))

def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})

def novaquestao(request):
    return render(request, 'votacao/novaquestao.html')

def gravarquestao(request):
    if request.method == 'POST':
        if request.POST.get('fnovaquestao'):
            questao = Questao()
            questao.questao_texto = request.POST['fnovaquestao']
            questao.pub_data= timezone.now()
            questao.save()
    #context = {'fnovaquestao':fnovaquestao}
            return HttpResponseRedirect(reverse('votacao:index'))

def novaopcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/nova_opcao.html',{'questao': questao})

def gravaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao = Opcao()
    opcao.opcao_texto = request.POST['fnovaopcao']
    opcao.votos = 0
    opcao.questao = questao
    opcao.save()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

def listarquestao(request):
    question_list = Questao.objects.all()
    context = {'question_list': question_list}
    return render(request, 'votacao/listar_questao.html', context)

def apagarquestao(request):
    try:
        questao = Questao.objects.get(pk=request.POST['questao'])
    except (KeyError, Questao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/listar_questao.html',  {'error_message': "Não escolheu uma opção"})
    else:
        questao.delete()
    return HttpResponseRedirect(reverse('votacao:index'))

def listaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/listar_opcao.html', {'questao': questao})

def apagaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/listar_opcao.html', {'questao': questao, 'error_message': "Não escolheu uma opção", })
    else:
        opcao_seleccionada.delete()

    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
