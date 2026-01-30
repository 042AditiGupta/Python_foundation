#oops:
#Imperative approach: a= 12 and b=12

a=12
b=12
print(a+b)

#Functional approach

def addition (a,b):
    print(a+b)
addition(2,3)
addition(1,4)

# oops- An object oriented paradigm is a programming paradigm 
# based on the concept of objects which can contain data(attributes) and methods(functions).

# class- a class is like a blueprint  or template for creating objects.

# attributes: variable inside the class are attributes
# methods: functions defined inside a class are methods

class Factory:
    a=12 #attribute
    def hello(self): #method
        print("bark")
    print("hello how are you i am getting initialized")
print(Factory().a)
Factory().hello()
     
# Object 

class Fruits:
    name="apple" #attribute
    def hello(self): #method
        print("apple is good for health")
    print("hello how are you i am getting initialized")

obj=Fruits()
print(obj.name)
obj.hello()
obj2=Fruits()

    
# constructor- a constructor is a method that runs automatically when we call a class
# and this constructor function will target the object location.

class Student:
    def __init__(self,name):
        self.name=name
s=Student("aditi")
print(s.name)

# self defines the location

class Factory:
    def __init__(self,material,zips,pockets):
        self.material=material  
        self.zips=zips  
        self.pockets=pockets
reebok=Factory("leather",3,3)
campus=Factory("nylon",3,3)
print(campus.pockets) 
print(campus.material)
print(reebok.material)

# attributes and methods inside class

class Factory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips  
        self.pockets=pockets
        
    def show(self):
        print(f"your objects are {self.material},{self.zips},{self.pockets}");

reebok=Factory("leather",2,3)
campus=Factory("nylon",3,3)
reebok.show()



    


