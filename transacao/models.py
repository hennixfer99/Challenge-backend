from django.db import models


class Escolhas(models.TextChoices):
    DEBITO = "Debito"
    BOLETO = "Boleto"
    FINANCIAMENTO = "Financiamento"
    CREDITO = "Credito"
    EMPRESTIMO = "Recebimento Emprestimo"
    VENDAS = "Vendas"
    TED = "Recebimento TED"
    DOC = "Recebimento DOC"
    ALUGUEL = "Aluguel"


class Transacoes(models.Model):
    type = models.CharField(max_length = 50, choices = Escolhas.choices)
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length = 11)
    card = models.CharField(max_length = 64)
    time = models.TimeField()
    owner_store = models.CharField(max_length = 248)
    store_name = models.CharField(max_length = 248)

