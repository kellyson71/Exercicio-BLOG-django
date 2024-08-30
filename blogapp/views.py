from django.shortcuts import render
from .models import Curso, Interesse, Projeto

# Create your views here.

def index(request):
    cursos = Curso.objects.all()
    interesses = Interesse.objects.all()
    projetos = Projeto.objects.all()
    return render(request, 'blogapp/index.html', {'cursos': cursos, 'interesses': interesses, 'projetos': projetos})

def sobre(request):
    return render(request, 'blogapp/sobre.html')
