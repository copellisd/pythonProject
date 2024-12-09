#Multilevel inheritace
#grandfather->father->son

class gf:
    gold="2kg"
    def bhk1(self):
        print("1bhk")
        print(self.gold)

class father(gf):
    diamond="22cart"
    def bhk2(self):
        print("2bhk")
        print(self.diamond)

class son(father):
    btc="1btc"
    def bhk3(self):
        print("3bhk")
        print(self.btc)

s=son()
print(s.gold)
print(s.diamond)
print(s.btc)

f=father()
#print(f.btc)#father not access son properties
print(f.gold)