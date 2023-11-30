from django.shortcuts import render
from .models import Produto

def index(request):
    prod =  Produto.objects.all()
    context = {
        'produtos': prod
    }
    return render(request, 'index.html', context)

def produto(request, id):
    prod = Produto.objects.get(id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def handler404(request, exception):
    return render(request, 'not_found.html')


def handler500(request):
    return render(request, 'erro500.html')

