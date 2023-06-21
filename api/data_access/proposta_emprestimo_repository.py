from api.data_access.base import RepositoryBase
from api.models import PropostaEmprestimo


class PropostaEmprestimoRepository(RepositoryBase):
    def __init__(self):
        super().__init__(PropostaEmprestimo)