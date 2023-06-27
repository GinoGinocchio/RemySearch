from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from Search.models import *
import os
# import pysolr
# from tika import parser

def home(request):
    return render (request, 'Search/Home.html')

def expediente(request):
    context = {}
    objetos = ArchivoPDF.objects.all()
    context['objetos'] = objetos
    return render (request, 'Search/exp.html', context = context)

# def index_pdf_to_solr(pdf_path, document_id):
#     solr = pysolr.Solr(os.environ['SOLR_SERVER'])

#     # Extraer el contenido del PDF utilizando Tika
#     parsed_pdf = parser.from_file(pdf_path)
#     content = parsed_pdf['content']

#     # Preparar los datos para enviar a Solr
#     doc = {
#         'id': document_id,
#         'content': content
#         # Agrega otros campos según tu esquema de Solr
#     }

