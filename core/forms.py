from django.forms import ModelForm
from .models import Prof
from .models import Aluno

#professores
class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = ['nome', 'data', 'materia']

#alunos

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','data','ano']
