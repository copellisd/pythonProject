class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# Create an instance of the class with the values 3 and 4
calculator = calc(3, 4)

# Call the methods on the instance
print(calculator.sum())  # Output: 7
print(calculator.sub())  # Output: -1
print(calculator.mul())  # Output: 12
print(calculator.div())  # Output: 0.75
