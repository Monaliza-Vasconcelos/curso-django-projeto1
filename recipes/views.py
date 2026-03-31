from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#HTTP request - cliente pede algo para o servidor
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Monaliza Vasconcelos'
    }) #render - servidor responde para o cliente com um template HTML     
    #return HttpResponse - servidor responde para o cliente
    #recipes/home.html - caminho do template HTML que será renderizado name espace do app recipes

def sobre(request):
    return HttpResponse("Página Sobre")

def contato(request):
    return HttpResponse("Página de Contato")