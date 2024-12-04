class bank:
    def  __init__(self,account_number,balance):
        self.balance=balance #public variable
        self.__account_number=account_number #private variable

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def show_me_account_number(self):#we create  this function to access private variable
        print(self.__account_number)#print that variable
    #def show_me_account_number(self,is_auth)
    #  if is_auth==true
    #      print(self.__account_number) #this process is in future we add authentication
    #  else
    #      print("not allowed")

icici=bank("1234567892",100)
icici.deposit(100)
icici.check_balance()
#print(icici.__account_number) we cant access.this is private variable.for that we follow some process
icici.show_me_account_number()
#icici.show_me_account_number(true)