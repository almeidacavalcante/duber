from src.domain.account import Account
from src.infrastructure.repository.account_repository import AccountRepository


class GetAccountUsecase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def get_account(self, account_id: str) -> Account:
        return self.account_repository.get(account_id)