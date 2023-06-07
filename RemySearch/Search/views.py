from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Fino")

def home(request):
    return render (request, 'Search/Home.html')