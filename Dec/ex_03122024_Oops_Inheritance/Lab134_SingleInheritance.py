class parent:
    gold="2kg"
    def bhk2(self):
      print("2bhk")
      print(self.gold)

class child(parent):
    diamond="diamond"
    def bhk3(self):
        print("3bhk")
        print(self.diamond)

ch_obj=child()
ch_obj.bhk2()
ch_obj.bhk3()

