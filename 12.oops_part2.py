#Attributes and methods

# Types of attributes - class Attribute and Instance Attribute

# Class Attribute
# A normal variable created inside a class is a class attribute and thats it

# Instance Attributes
# A attribute created using an instance like self.name,self.age etc

# Example

class Animal:
    name="Tiger" # class Attribute
    
    def __init__(self,age):
        self.age=age #Instance attribute
        
    def show(self): #Instance method
        print(f"I am instance method and my age is {self.age}")
        
    @classmethod
    def hello(cls): #cls will target the class location
        print("how is the weather'it's very cold outside") #class method
        
    @staticmethod
    def static():
        print("static method use decorator i.e staticmethod")
        
obj=Animal(12)
obj.show()
obj.static()
obj.show()
