from abc import ABC, abstractmethod


class ExcelReader(ABC):
    @abstractmethod
    def readfromExcel(self):
        pass

class browser(ExcelReader):
    @abstractmethod
    def startbrowser(self):
        pass

    @abstractmethod
    def stopbrowser(self):
        pass

class tc1(browser):

    def startbrowser(self):
        print("starting the browser")

    def stopbrowser(self):
        print("stoping the browser")

    def readfromExcel(self):
        print("read from excel is ready")

    def runtc(self):

        self.startbrowser()
        self.readfromExcel()
        self.stopbrowser()

t=tc1()
t.runtc()