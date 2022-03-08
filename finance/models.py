from django.db import models

class Categorie(models.Model):
    """Representation of the categories of each expense"""
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        ordering = ['name']
        db_table = 'categorie'
        verbose_name = 'Categorie'
        
    def __str__(self):
        return self.name


class Expense(models.Model):
    """Representation of all user expense"""
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=8)
    
    class Meta:
        ordering = ['date', 'value']
        db_table = 'expense'
        verbose_name = 'Expense'
        
    def __str__(self):
        return self.description


class Revenue(models.Model):
    """Representation of all user revenue"""
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ['date', 'value']
        db_table = 'revenue'
        verbose_name = 'Revenue'
        
    def __str__(self):
        return self.description