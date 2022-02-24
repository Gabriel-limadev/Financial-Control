from django.db import models

class Categoria(models.Model):
    """Representação das categorias de cada despesa"""
    nome = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ['nome']
        db_table = 'categoria'
        verbose_name = 'Categoria'
        
    def __str__(self):
        return self.nome


class Despesa(models.Model):
    """Representação de toda despesa do usuário"""
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=8)
    
    class Meta:
        ordering = ['data', 'valor']
        db_table = 'despesa'
        verbose_name = 'Despesa'
        
    def __str__(self):
        return self.descricao


class Receita(models.Model):
    """Representação de toda receita do usuário"""
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()

    class Meta:
        ordering = ['data', 'valor']
        db_table = 'receita'
        verbose_name = 'Receita'
        
    def __str__(self):
        return self.descricao