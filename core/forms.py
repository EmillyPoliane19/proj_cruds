from django.forms import ModelForm
from .models import Prof


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = ['nome', 'data', 'materia', 'image']

