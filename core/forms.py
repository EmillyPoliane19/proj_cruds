from django.forms import ModelForm
from .models import Prof,Aluno,Curso 

#professores
class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = ['nome', 'data', 'materia', 'image']

#alunos

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','data','ano']

#cursos

class CursosForm(ModelForm):
    class Meta:
           model = Curso
           fields = ['nome', 'vagas','hora']

