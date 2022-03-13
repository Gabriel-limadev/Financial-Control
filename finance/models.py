from django.db import models

class Expense(models.Model):
    """Representation of all user expense"""
    CATEGORIE = (
        ('F', 'Food'),
        ('H', 'Health'),
        ('T', 'Transport'),
        ('E', 'Education'),
        ('L', 'Leisure'),
        ('O', 'Others')
    )

    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField()
    categorie = models.CharField(max_length=1, choices=CATEGORIE, default='A')
    
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