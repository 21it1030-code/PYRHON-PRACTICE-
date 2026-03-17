# ABSTRACTION
from abc import ABC,abstractmethod
class Transaction(ABC):
    @abstractmethod
    def payment(self):
        print("paying using phonepay")

    @abstractmethod
    def Cash(self):
        print("cashhhhh")


class Transfer(ABC):
    def payment(self):
        print("paying with cash")

    def Cash(self):
        print("cash")
        

t1=Transfer()
t1.Cash()
