from django.urls import path
from recipes.views import home, sobre, contato


urlpatterns = [
    path('', home), #Home page
    path('sobre/', sobre), #Página sobre
    path('contato/', contato) #Página de contato
]