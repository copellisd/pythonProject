#custom Exception

class lowBalanceExceptionCustom(Exception):

    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=100
withdraw=int(input("enetr withdraw value"))
if withdraw>balance:
    raise lowBalanceExceptionCustom("balance low")
else:
    print("balance is",(balance-withdraw))