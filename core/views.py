from cgitb import reset
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Prof, Aluno, Curso
from .forms import ProfForm, AlunoForm, CursosForm

def home(request):
    return render(request,'pagina_inicial.html')
    
#CRUD DOS PROFESSORES
def listar_prof(request):
    professores = Prof.objects.all()
    contexto = {
        'todos_prof': professores
    }
    return render(request, 'lista_profs.html', contexto)

def cadastrar_prof(request):
    form = ProfForm(request. POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_prof')

    contexto = {
        'form_prof': form
    }
    return render(request, 'cadastro_prof.html', contexto)

def editar_prof(request, id):
    professor = Prof.objects.get(pk=id)
    
    form = ProfForm(request.POST or None, instance=professor)
   
    if form.is_valid():
        form.save()
        return redirect('listar_prof')
    
    contexto = {
        'form_prof': form
    }

    return render(request, 'cadastro_prof.html', contexto)

def remover_prof(request, id):
    professor = Prof.objects.get(pk=id)
    professor.delete()
    return redirect('listar_prof')

#CRUD DOS ALUNOS
def listar_aluno(request):
    alunos = Aluno.objects.all()
    contexto = {
        'todos_alunos': alunos
    }
    return render(request,'cadastro_alunos.html', contexto)

def cadastrar_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_aluno')

    contexto = {
        'form_aluno': form
    }
    return render(request, 'cadastrar_aluno.html', contexto)

def editar_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('listar_aluno')

    contexto = {
        'form_aluno': form
    }
    return render(request, 'cadastrar_aluno.html', contexto)

def remover_aluno(request,id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return redirect('listar_aluno')

#CRUD CURSOS

def cursos_cadastrar (request):
    form = CursosForm (request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cursos_cadastrar')
    contexto = {
      'form_curso': form 
    }
    return render (request,'Cadastrar_Cursos.html', contexto)
