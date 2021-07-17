from django.shortcuts import render, redirect
from .forms import(
    MedicoForm,
    PostoForm,
    FolgaForm,
    EscalaForm
)
from core.models import (
    Medico,
    Posto,
    Folga,
    Escala,
)
import datetime
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
from django.views.generic.base import View


def home(request):
    msg = {'mensagem':'ola mundo'}   
    return render(request, 'core/index.html', msg)


def lista_medicos(request):
    medicos = Medico.objects.all().filter(disponivel=True)
    form = MedicoForm()
    data = {'medicos': medicos, 'form': form}
    return render(request, 'core/lista_medicos.html', data)


def medico_novo(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = 'Médico cadastrado com sucesso!'
        medicos = Medico.objects.all()
        data = {'medicos': medicos, 'form': form, 'sucesso':sucesso }
        return render(request, 'core/lista_medicos.html', data)
    return redirect('core_lista_medicos')


def medico_update(request, id):
    data = {}
    medico = Medico.objects.get(id=id)
    form = MedicoForm(request.POST or None, instance=medico)
    data['medico'] = medico
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_medicos')
    else:
        return render(request, 'core/update_medico.html', data)

#POSTOS
def lista_postos(request):
    postos = Posto.objects.all().filter(disponivel=True) # listo apenas os disponiveis, para deletar somente django admin, ou no db.
    form = PostoForm()
    data = {'postos': postos, 'form': form}
    return render(request, 'core/lista_postos.html', data)


def posto_novo(request):
    form = PostoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = 'Posto cadastrado com sucesso!'
        postos = Posto.objects.filter(disponivel=True)
        data = {'postos': postos, 'form': form, 'sucesso':sucesso }
        return render(request, 'core/lista_postos.html', data)
    return redirect('core_lista_postos')


def posto_update(request, id): 
    data = {}
    posto = Posto.objects.get(id=id)
    form = PostoForm(request.POST or None, instance=posto)
    data['posto'] = posto
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_postos')
    else:
        return render(request, 'core/update_posto.html', data)

#ESCALAS
def lista_escalas(request):
    escalas = Escala.objects.all().filter(disponivel=True)
    form = EscalaForm()
    data = {'escalas': escalas, 'form': form}
    return render(request, 'core/lista_escalas.html', data)


def escala_novo(request):
  
    form = EscalaForm(request.POST or None) 

    medico_id = form.data.get("medico") 
    
    try:
        if medico_id:
            escala_digitada = form.data.get("data") 
            escala_digitada = datetime.datetime.strptime(escala_digitada,
                                                    '%d/%m/%Y').date() 

            existe_folga = Folga.objects.filter(data=escala_digitada,  
                                            medico_id=medico_id)

            if existe_folga:
                erro = " Já existe folga para esse medico nessa data, " \
                    "favor selecione outro medico ou outra data!"
                escalas = Escala.objects.filter(disponivel=True) 
                data = {'escalas': escalas, 'form': form, 'erro': erro} 
                return render(request, 'core/lista_escalas.html', data)

    except Exception as e:
        erro = " Formato de data inálido, ex: 10/10/2010 "
        escalas = Escala.objects.filter(disponivel=True) 
        data = {'escalas': escalas, 'form': form, 'erro': erro}
        return render(request, 'core/lista_escalas.html', data)


    if form.is_valid():
        form.save()    
        sucesso = 'Escala cadastrada com sucesso!'
        escalas = Escala.objects.filter(disponivel=True)
        data = {'escalas': escalas, 'form': form, 'sucesso':sucesso }
        return render(request, 'core/lista_escalas.html', data)
    return redirect('core_lista_escalas')


def escala_update(request, id):
    data = {}
    escala = Escala.objects.get(id=id)
    form = EscalaForm(request.POST or None, instance=escala)
    data['escala'] = escala 
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_escalas')
    else:
        return render(request, 'core/update_escala.html', data)

def escala_delete(request, id):
    escala = Escala.objects.get(id=id)
    if request.method == 'POST':
        escala.delete()
        return redirect('core_lista_escalas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': escala})

#CADASTRO FOlGAS
def lista_folgas(request):
    folgas = Folga.objects.all()
    form = FolgaForm()
    data = {'folgas': folgas, 'form': form}
    return render(request, 'core/lista_folgas.html', data)


def folga_novo(request):
    form = FolgaForm(request.POST or None)

    escala_id = form.data.get("medico")

    try:
        if escala_id:
            folga_digitada = form.data.get("data")
            folga_digitada = datetime.datetime.strptime(folga_digitada,
                                                        '%d/%m/%Y').date()

            existe_escala = Escala.objects.filter(data=folga_digitada,
                                                medico_id=escala_id)

            if existe_escala:
                erro = 'Medico não pode folgar nesse dia ' \
                    'pois ele tem escala de trabalho!'
                folgas = Folga.objects.all()
                data = {'folgas': folgas, 'form': form, 'erro': erro}
                return render(request, 'core/lista_folgas.html', data)

    except Exception as e:
        erro = " Formato de data inálido, ex: 10/10/2010 "
        folgas = Folga.objects.all()
        data = {'folgas': folgas, 'form': form, 'erro': erro}
        return render(request, 'core/lista_folgas.html', data)


    if form.is_valid():
        form.save()
        sucesso = 'Folga cadastrada com sucesso!'
        folgas = Folga.objects.all()
        data = {'folgas': folgas, 'form': form, 'sucesso':sucesso }
        return render(request, 'core/lista_folgas.html', data)
    return redirect('core_lista_folgas')
   

def folga_update(request, id):
    data = {}
    folga = Folga.objects.get(id=id)
    form = FolgaForm(request.POST or None, instance=folga)
    data['folga'] = folga
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_folgas')
    else:
        return render(request, 'core/update_folgas.html', data)


def folga_delete(request, id):
    folga = Folga.objects.get(id=id)
    if request.method == 'POST':
        folga.delete()
        return redirect('core_lista_folgas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': folga})


#PDFs
class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str): 
        
        template = get_template(path)  #16               

        html = template.render(params)         
        
        response = io.BytesIO()

        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)                      
        
        if not pdf.err: 
            response = HttpResponse( 
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class PdfEscalas(View):                 

    def get(self, request):           
        escalas = Escala.objects.all()  
        params = {                     
            'escalas': escalas,
            'request': request,
        }
        return Render.render('core/relatorio_escalas.html', params, 'relatorio-escalas')

# Utilizando dessa forma eu vou poder ter ela uma vez só e reutilizar no sitema inteiro, qualquer lugar
# no sistema que eu fizer essa chamada passando o html e os parametros, ela vai gerar o pdf.