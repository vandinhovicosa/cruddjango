from django.db import models

# Create your models here.

class endereco(models.Model):
    logradouro = models.CharField(max_length=255, blank=False, null=False)
    bairro = models.CharField(max_length=255, blank=False, null=False)
    cidade = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(null=False, blank=False)
    cep = models.CharField(max_length=10, null=False, blank=False)    
