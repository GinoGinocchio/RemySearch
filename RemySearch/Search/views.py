from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from Search.models import *
import os

def home(request):
    return render (request, 'Search/Home.html')

def expediente(request):
    context = {}
    objetos = ArchivoPDF.objects.all()
    context['objetos'] = objetos
    return render (request, 'Search/exp.html', context = context)

