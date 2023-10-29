from sqlalchemy.orm import Session

from src.domain.account import Account
from src.infrastructure.models import AccountModel
from src.infrastructure.repository.account_repository import AccountRepository


class AccountRepositoryDatabase(AccountRepository):
    def __init__(self, session: Session):
        self.session = session

    def get(self, account_id: str):
        return self.session.query(AccountModel).filter(AccountModel.account_id == account_id).first()

    def save(self, account: Account):
        orm_account = self.to_orm_model(account)
        self.session.add(orm_account)
        self.session.commit()
        return self.to_domain_entity(orm_account)

    @staticmethod
    def to_domain_entity(orm_entity: AccountModel) -> Account:
        return Account(
            name=orm_entity.name,
            email=orm_entity.email,
            cpf=orm_entity.cpf,
            is_passenger=orm_entity.is_passenger,
            is_driver=orm_entity.is_driver,
            car_plate=orm_entity.car_plate,
        )

    @staticmethod
    def to_orm_model(domain_entity: Account) -> AccountModel:
        return AccountModel(
            name=domain_entity.name,
            email=domain_entity.email,
            cpf=domain_entity.cpf,
            is_passanger=domain_entity.is_passenger,
            is_driver=domain_entity.is_driver,
            car_plate=domain_entity.car_plate,
        )
