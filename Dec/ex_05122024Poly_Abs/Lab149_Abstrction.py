#ABSTRACTION=python imports n creates ABC Class -abstract base class
#hide the details and show what are we required
from abc import ABC, abstractmethod


class animal(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):
    def make_sound(self):
        print("bark bark bark....")

d=dog("shera")
d.make_sound()
