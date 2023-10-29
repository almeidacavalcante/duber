from bradocs4py import CPF


class DocumentValidators:
    @staticmethod
    def is_valid_cpf(cpf: str):
        return CPF(cpf).isValid
