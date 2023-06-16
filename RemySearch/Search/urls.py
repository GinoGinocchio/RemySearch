from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('expedientes/', expediente, name='expediente'),
    path('media/pdf/<pk>/', pdf_view, name='pdf_view'),
]

