from abc import ABC, abstractmethod


class father(ABC):

    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass

class son(father):

    def loan(self):
        print("1L")


s=son("parmod")
s.loan()




