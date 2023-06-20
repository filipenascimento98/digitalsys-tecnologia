from rest_framework import serializers


class PropostaEmprestimoSerializer(serializers.Serializer):
    nome_completo = serializers.CharField()
    cpf = serializers.CharField()
    endereco = serializers.CharField()
    valor_emprestimo_solicitado = serializers.FloatField()

    def validate_cpf(self, value):
        """
            Checa se o CPF é válido.
        """
        # Remover caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, cpf))

        # Verificar se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return serializers.ValidationError("CPF inválido.")

        # Verificar se todos os dígitos são iguais (CPF inválido)
        if cpf == cpf[0] * 11:
            return serializers.ValidationError("CPF inválido.")

        # Calcular o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10) % 11 if soma * 10 % 11 != 10 else 0

        # Verificar o primeiro dígito verificador
        if primeiro_digito != int(cpf[9]):
            return serializers.ValidationError("CPF inválido.")

        # Calcular o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito = (soma * 10) % 11 if soma * 10 % 11 != 10 else 0

        # Verificar o segundo dígito verificador
        if segundo_digito != int(cpf[10]):
            return serializers.ValidationError("CPF inválido.")

        return value
    
    def validate_valor_emprestimo_solicitado(self, value):
        if value < 0:
            raise serializers.ValidationError("Valos de empréstimo inválido.")