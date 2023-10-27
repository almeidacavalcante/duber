from bradocs4py import CPF

from src.domain.exceptions.domain_exception import DomainException


class DocumentValidators:
    @staticmethod
    def is_valid_cpf(cpf: str):
        return CPF(cpf).isValid
