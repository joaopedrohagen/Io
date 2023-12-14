from django.db import models

# Create your models here.
class CEP (models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    localidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)

def __str__(self):
    return self.cep

