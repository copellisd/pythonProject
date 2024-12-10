from abc import ABC, abstractmethod


class gearbox(ABC):
    @abstractmethod
    def set_gear(self):
        pass

class engine(gearbox):
    @abstractmethod
    def start(self):
        super().set_gear()

        pass
    @abstractmethod
    def stop(self):
        pass

class car(engine):

    def start(self):

        print("starting")
    def stop(self):
        print("stopping")
    def set_gear(self):
        print("gera is ready")

    def drive(self):
        self.start()
        self.stop()


c=car()
c.drive()