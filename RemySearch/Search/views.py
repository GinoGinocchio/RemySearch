from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, 'Search/Home.html')

def expediente(request):
    return render (request,'Search/exp.html')