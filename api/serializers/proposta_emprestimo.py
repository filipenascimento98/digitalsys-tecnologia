import re
from rest_framework import serializers


class PropostaEmprestimoSerializer(serializers.Serializer):
    nome_completo = serializers.CharField()
    cpf = serializers.CharField()
    endereco = serializers.CharField()
    valor_emprestimo_solicitado = serializers.FloatField()

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError("CPF inválido.")
        return value 
    
    def validate_valor_emprestimo_solicitado(self, value):
        if value <= 0:
            raise serializers.ValidationError("Valor de empréstimo inválido.")
        
        return value