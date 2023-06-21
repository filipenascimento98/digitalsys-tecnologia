from django.contrib import admin
from api.models import PropostaEmprestimo


class PropostaEmprestimoAdmin(admin.ModelAdmin):
    list_display = ("nome_completo", "valor_emprestimo_solicitado", "aprovado", "created_at")

admin.site.register(PropostaEmprestimo, PropostaEmprestimoAdmin)
