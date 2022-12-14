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
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, editar_prof, listar_prof, cadastrar_prof, remover_prof, listar_aluno, cadastrar_aluno, editar_aluno, remover_aluno, listar_cursos, cursos_cadastrar, editar_curso, remover_curso



urlpatterns = [
    #url da pag. ininial
    path('home/', home, name='home' ),

    #url das pag. aluno
    path('cadastrar_aluno/', cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', listar_aluno, name='listar_aluno'),
    path('alunos_editar/<int:id>/', editar_aluno, name='editar_aluno'),
    path('aluno_remover/<int:id>/', remover_aluno, name='remover_aluno'),

    #url das pag. professor
    path('cadastrarprof/', cadastrar_prof, name='cadastrar_prof'),
    path('listarprof/', listar_prof, name='listar_prof'),
    path('editarprof/<int:id>/', editar_prof, name='editar_prof'),
    path('removerprof/<int:id>/', remover_prof, name='remover_prof'),

    #url das pag. das pag cursos
    path('lista_cursos/', listar_cursos, name='listar_cursos'),
    path('cursos_cadastrar/', cursos_cadastrar, name='cursos_cadastrar'),
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
    path('remover_curso/<int:id>/', remover_curso, name='remover_curso'),

    #url pag. admin.
    path('admin/', admin.site.urls),

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

