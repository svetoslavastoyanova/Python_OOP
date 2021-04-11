from abc import ABC, abstractmethod


class BaseDecoration:
    @abstractmethod
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

