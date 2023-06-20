from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.serializers.proposta_emprestimo import PropostaEmprestimoSerializer
from api.tasks import avalia_emprestimo


class PropostaEmprestimoView(generics.GenericAPIView):
    serializer_class = PropostaEmprestimoSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            try:
                avalia_emprestimo.delay()
            except Exception as e:
                print(e)
                return Response(
                    {'message': 'Ocorreu um erro inesperado.'},
                    status=status.HTTP_412_PRECONDITION_FAILED
                )

        return Response(status=status.HTTP_201_CREATED)