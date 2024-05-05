from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# request handler
# request----- response

def hola_mundo(request):
    return render(request, 'hola.html', {'name': 'Diego' })