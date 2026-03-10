from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'associado/index.html')

def perfil(request):
   return render(request, 'associado/perfil.html')