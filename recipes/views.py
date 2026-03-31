from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#HTTP request - cliente pede algo para o servidor
def home(request):
    return HttpResponse("Home Page - Projeto Django")
    #return HttpResponse - servidor responde para o cliente

def sobre(request):
    return HttpResponse("Página Sobre")

def contato(request):
    return HttpResponse("Página de Contato")