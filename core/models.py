from django.db import models

class Prof(models.Model):
   nome = models.CharField('Nome', max_length=100)
   data = models.DateField('Data de nascimento')
   materia = models.CharField('Matéria', max_length=100)
   foto = models.ImageField('Foto', upload_to='upload', null=True)

class Curso(models.Model):
   nome = models.CharField('Nome', max_length=100)
   vagas = models.IntegerField('vagas')
   hora = models.IntegerField('hora')

class Aluno(models.Model):
   nome = models.CharField('Nome', max_length=100)
   data = models.DateField('Data de Nascimento')
   ano  = models.IntegerField('Ano Letivo')
