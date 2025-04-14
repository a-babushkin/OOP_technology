from abc import ABC, abstractmethod
from typing import Any


class BaseCatOrder(ABC):
    @abstractmethod
    def add_product(self, *args: Any, **kwargs: Any) -> None:
        pass
