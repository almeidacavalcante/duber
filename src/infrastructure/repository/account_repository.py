from abc import abstractmethod, ABC

from src.domain.account import Account


class AccountRepository(ABC):
    @abstractmethod
    def save(self, account: Account):
        pass

    @abstractmethod
    def get(self, account_id: str):
        pass