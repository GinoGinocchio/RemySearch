from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from Search.models import *
import os

def home(request):
    return render (request, 'Search/Home.html')

def expediente(request):
    return render (request,'Search/exp.html')

def pdf_view(request, pk):
    archivo_pdf = get_object_or_404(ArchivoPDF, pk=pk)
    pdf_path = os.path.join(settings.MEDIA_ROOT, archivo_pdf.archivo.name)

    with open(pdf_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{archivo_pdf.archivo.name}"'
        return response
