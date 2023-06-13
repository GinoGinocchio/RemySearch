from django.urls import path
from .views import *

urlpatterns = [
    path('expedientes/', home, name='home'),
    path('', expediente, name='expediente'),
]

