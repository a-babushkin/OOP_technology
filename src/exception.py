class ZeroQuantityProduct(Exception):

    def __init__(self, message: str = "Количество не указано!") -> None:
        super().__init__(message)
