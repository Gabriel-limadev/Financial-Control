from django.db import models

# Create your models here.

class Receita(models.Model):
    descricao = models.CharField(max_length=254)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()

    class Meta:
        ordering = ['data']
        
    def __str__(self):
        return self.descricao