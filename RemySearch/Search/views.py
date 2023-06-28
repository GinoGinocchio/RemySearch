from django.shortcuts import render
from django.conf import settings
from Search.models import *
from .forms import BusquedaForm
import pysolr


def home(request):
    return render (request, 'Search/Home.html')

def expediente(request):
    context = {}
    objetos = ArchivoPDF.objects.all()
    context['objetos'] = objetos
    return render (request, 'Search/exp.html', context = context)

def buscar_documentos(palabra_clave):
    solr = pysolr.Solr(settings.SOLR_SERVER)
    query = f'content:*{palabra_clave}* OR id:*{palabra_clave}*'
    resultados = solr.search(query, sort='score desc',fl='id')
    return resultados

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            palabra_clave = form.cleaned_data['palabra_clave']
            resultados_solr = buscar_documentos(palabra_clave)
            ids = [int(result['id']) for result in resultados_solr]
            resultados_modelo = ArchivoPDF.objects.in_bulk(ids)
            objetos_ordenados = [resultados_modelo[id] for id in ids if id in resultados_modelo]
            return render(request, 'Search/exp.html', {'resultados': objetos_ordenados, 'form': form})
    else:
        form = BusquedaForm()
        resultados_modelo = ArchivoPDF.objects.all()
        return render(request, 'Search/exp.html', {'resultados': resultados_modelo, 'form': form})
    