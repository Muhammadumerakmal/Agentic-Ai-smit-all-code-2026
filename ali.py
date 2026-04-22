class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")

p1 = Person("Ali", 17)
p1.greet()      
p1.birthday()  
p1.greet()      