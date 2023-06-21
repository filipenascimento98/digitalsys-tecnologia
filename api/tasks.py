from __future__ import absolute_import, unicode_literals
from celery import shared_task
from api.domain.proposta_emprestimo import PropostaEmprestimoDomain


@shared_task
def avalia_emprestimo(data):
    domain = PropostaEmprestimoDomain()

    #Algoritmo para manter metade das propostas aprovadas e a outra metade reprovada
    propostas = domain.list(sort_by_field='created_at')
    if propostas['status'] == 200 and len(propostas['message']) > 0:
        ultima_proposta = propostas['message'][0]
        data['aprovado'] = not ultima_proposta.aprovado
    else:
        data['aprovado'] = True
        
    domain.create(data)