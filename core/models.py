from django.db import models

class Prof(models.Model):
   nome = models.CharField('Nome', max_length=100)
   data = models.DateField('Data de nascimento')
   materia = models.CharField('Matéria', max_length=100)

