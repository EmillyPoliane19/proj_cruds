from django.db import models

class Prof(models.Model):
   nome = models.CharField('Nome', max_length=100)
   data = models.DateField('Data de nascimento')
   materia = models.CharField('Matéria', max_length=100)

class Aluno(models.Model):
   nome = models.CharField('Nome', max_length=100)
   data = models.DateField('Data de Nascimento')
   ano  = models.IntegerField('Ano Letivo')
   materia = models.CharField('Matérias', max_length=100)
