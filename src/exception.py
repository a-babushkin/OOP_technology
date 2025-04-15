class ZeroQuantityProduct(Exception):

    def __init__(self, message="Количество не указано!"):
        super().__init__(message)