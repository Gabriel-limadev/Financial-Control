from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Despesa(models.Model):
    descricao = models.CharField(max_length=254)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()  
    
    class Meta:
        ordering = ['data']
        
    def __str__(self):
        return self.descricao
        
