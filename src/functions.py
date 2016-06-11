from abc import ABCMeta, abstractmethod


class Polynomial(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self): pass


class Number(Polynomial):
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self


class Sum(Polynomial):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calculate(self):
        return Number(self.left.value + self.right.value)
