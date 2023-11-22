class MathOperations:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Выполняется сложение")
        return self.value + other.value

    def __sub__(self, other):
        print("Выполняется вычитание")
        return self.value - other.value

    def __mul__(self, other):
        print("Выполняется умножение")
        return self.value * other.value

    def __truediv__(self, other):
        print("Выполняется деление")
        return self.value / other.value
