class person:

    def __init__(self,name):
        self.name=name  

    def walk(self):
        return self.name

datta=person("datta")
gang=person("gang")

print(datta.name)
print(gang.name)

print(datta.walk())
print(gang.walk())