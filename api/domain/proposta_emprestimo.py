from api.domain.base import DomainBase
from api.data_access.proposta_emprestimo_repository import PropostaEmprestimoRepository


class PropostaEmprestimoDomain(DomainBase):
    def __init__(self):
        super().__init__(PropostaEmprestimoRepository())