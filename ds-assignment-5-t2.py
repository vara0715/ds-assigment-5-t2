class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num2 / self.num1
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
obj=Calculator(num1,num2)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())
