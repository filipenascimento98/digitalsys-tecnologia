from django.db import models
from django.core.validators import MinValueValidator


class PropostaEmprestimo(models.Model):
    nome_completo = models.CharField("Nome Completo", max_length=75)
    cpf = models.CharField("CPF", max_length=11)
    endereco = models.CharField("Endereço", max_length=100)
    valor_emprestimo_solicitado = models.FloatField(validators=[MinValueValidator(0)])
    aprovado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
