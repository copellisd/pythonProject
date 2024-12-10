
#multiple inheritance means u can collect money from both father n mother
class  father:
    def home(self):
        print("home")
    def father_money(self):
        return 5
class mother:
    def home(self):
        print("home")
    def mother_money(self):
        return 2

class son(father,mother):
    def print(self):
        print("son")

s=son()
print(s.mother_money())
print(s.father_money())

#in case of same method interpreter access first  one .here father n mother
# in son method father is 1st one right.
print(s.home())#gets fathers home