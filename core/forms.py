from django.forms import ModelForm
from .models import Prof, Curso 


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = ['nome', 'data', 'materia']


class CursosForm(ModelForm):
    class Meta:
           model = Curso
           fields = ['nome', 'vagas','hora']

