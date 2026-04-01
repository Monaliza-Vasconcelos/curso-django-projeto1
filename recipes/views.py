from django.shortcuts import render

# Create your views here.

#HTTP request - cliente pede algo para o servidor
def home(request):
    return render(request, 'recipes/pages/home.html', {
        'name': 'Monaliza Vasconcelos'
    }) #render - servidor responde para o cliente com um template HTML     
    #return HttpResponse - servidor responde para o cliente
    #recipes/home.html - caminho do template HTML que será renderizado name espace do app recipes
