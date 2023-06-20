from django.urls import path

from api.views.proposta_emprestimo import PropostaEmprestimoView


urlpatterns = [
    path('proposta-emprestimo/', PropostaEmprestimoView.as_view(), name='proposta-emprestimo')
]