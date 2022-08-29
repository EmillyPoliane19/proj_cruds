"""proj_cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import editar_prof, listar_prof, cadastrar_prof, remover_prof, cursos_cadastrar



urlpatterns = [

    path('cadastrar_aluno', cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', listar_aluno, name='listar_cursos'),
    path('cadastrarprof/', cadastrar_prof, name='cadastrar_prof'),
    path('listarprof/', listar_prof, name='listar_prof'),
    path('editarprof/<int:id>/', editar_prof, name='editar_prof'),
    path('removerprof/<int:id>/', remover_prof, name='remover_prof'),
    path ('cursos_cadastrar/', cursos_cadastrar, name='cursos_cadastrar'),
    path('admin/', admin.site.urls),
]
