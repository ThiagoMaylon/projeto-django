from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome do Produto', max_length=100)
    preco = models.DecimalField('Preço do Produto', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
