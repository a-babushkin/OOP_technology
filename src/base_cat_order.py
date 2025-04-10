from abc import ABC, abstractmethod


class BaseCatOrder(ABC):
    @abstractmethod
    def add_product(self, *args, **kwargs) -> None:
        pass
