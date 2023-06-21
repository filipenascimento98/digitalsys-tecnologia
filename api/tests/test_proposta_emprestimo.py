from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from api.data_access.proposta_emprestimo_repository import PropostaEmprestimoRepository


class PropostaEmprestimoTest(TestCase):
    def setUp(self):
        self.proposta_emprestimo_repository = PropostaEmprestimoRepository()
        self.proposta = {
            "nome_completo": "Pessoa A",
            "cpf": "00000000000",
            "endereco": "Rua A",
            "valor_emprestimo_solicitado": 10
        }
        self.api_client = APIClient()
    
    def test_create_proposta(self):
        """
        POST - Cria uma proposta
        """
        response = self.api_client.post(reverse('proposta-emprestimo'), self.proposta, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_proposta_cpf_invalid(self):
        """
        Tenta criar uma proposta com CPF inválido
        """
        self.proposta['cpf'] = "0"
        response = self.api_client.post(reverse('proposta-emprestimo'), self.proposta, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_proposta_valor_invalido(self):
        """
        Tenta criar uma proposta com valor de empréstimo inválido(menor ou igual a 0)
        """
        self.proposta['valor_emprestimo_solicitado'] = 0
        response_valor_zero = self.api_client.post(reverse('proposta-emprestimo'), self.proposta, format='json')
        self.proposta['valor_emprestimo_solicitado'] = -1
        response_valor_negativo = self.api_client.post(reverse('proposta-emprestimo'), self.proposta, format='json')

        self.assertEqual(response_valor_zero.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_valor_negativo.status_code, status.HTTP_400_BAD_REQUEST)
        