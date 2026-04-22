# # # # Task 1 (Lesson 01–02): Apna ek "bio card" print karo — naam, age, city, aur kya ban'na chahte ho. Sirf print() aur variables use karo.

# # # # my_bio = "my name is umer akmal , my age is 18, i live in karachi and i want to become a full stack web developer"

# # # # print(my_bio)


# # # # Task 2 (Lesson 03): Ek number lo. Agar 18 se zyada hai toh "adult" print karo, agar 13 se zyada hai toh "teen", warna "kid".

# # # # age = 13

# # # # if age >= 18:
# # # #     print("adult🧑")

# # # # else:
# # # #     print("kid👶")    


# # # # Task 3 (Lesson 04): 1 se 10 tak loop chalao. Sirf even numbers print karo.

# # # # for i in range(1,11):
# # # #     if i % 2 == 0:
# # # #         print(i)


# # # # Task 4 (Lesson 05): add(a, b) function banao with type hints — def add(a: int, b: int) -> int. Phir multiply bhi banao.

# # # # def add(a:int,b:int)->int:
# # # #     return a+b

# # # # def multiply(a:int,b:int)->int:
# # # #     return a*b


# # # # print(add(5,9))
# # # # print(multiply(5,9))



# # # # Task 5 (Lesson 06–07): Apni favourite 5 tech skills ki list banao. Phir ek dict banao jisme skill name key ho aur experience (years) value ho.

# # # # tech_list = ["js","py","ts","css","html"]

# # # # tech_dict = {
# # # #     "skill":"full stack dev",
# # # #     "exp":3
# # # # }

# # # # print(tech_list)
# # # # print(tech_dict)



# # # # # tech_dict = {
# # # # #     "JavaScript": 3,
# # # # #     "Python": 2,
# # # # #     "TypeScript": 1,
# # # # #     "CSS": 3,
# # # # #     "HTML": 4
# # # # # }

# # # # # Yahan loop chalao aur print karo:
# # # # # "JavaScript → 3 years experience"
# # # # # "Python → 2 years experience"
# # # # # ... aur baaki sab



# # # # # tech_dict = {
# # # # #    "JavaScript": 3,
# # # # #     "Python": 2,
# # # # #    "TypeScript": 1,
# # # # #    "CSS": 3,
# # # # #    "HTML": 4
# # # # # }


# # # # # for i in tech_dict:
# # # # #     print(f"{i} → {tech_dict[i]} years experience")



# # # # # # Ek function banao: get_expert_skills(skills: dict) -> list
# # # # # Jo sirf woh skills return kare jisme experience 2 se zyada ho
# # # # # Example output: ["JavaScript", "CSS", "HTML"]

# # # # # def get_expert_skills(skills:dict)->list:
# # # # #     expert_skills = []
# # # # #     for i in skills:
# # # # #         if skills[i] >= 2:
# # # # #             expert_skills.append(i)
# # # # #     return expert_skills



# # # # # print(get_expert_skills({
# # # # #     "JavaScript": 3,
# # # # #     "Python": 2,
# # # # #     "TypeScript": 1,
# # # # #     "CSS": 3,
# # # # #     "HTML": 4}))


# # # # # # Ek function banao: divide(a: int, b: int) -> float
# # # # # Agar b = 0 ho toh crash mat karo
# # # # # Gracefully handle karo aur message print karo:
# # # # # "Error: 0 se divide nahi kar sakte!"


# # # # def divide(a:int,b:int)->float:
# # # #     try:
# # # #         return a/b
# # # #     except ZeroDivisionError as e:
# # # #         print("cant divide by zero")

# # # # divide(5,0)        


# # # # def eat(noodles:int)->int:
# # # #    return noodles * 2








# # # # 









# # # # class Person:
# # # #     def __init__(self, name):
# # # #         self.name = name     # Public attribute, Instance Variable
# # # #         self.state = "Idle"  # Default state

# # # #     def running(self):
# # # #         self.state = "Running"
# # # #         print(f"{self.name} is now running.")

# # # #     def walking(self):
# # # #         self.state = "Walking"
# # # #         print(f"{self.name} is now walking.")

# # # #     def sleeping(self):
# # # #         self.state = "Sleeping"
# # # #         print(f"{self.name} is now sleeping.")

# # # #     def show_state(self):
# # # #         print(f"{self.name} is currently in '{self.state}' state.")



# # # # oops (object-oriented programming)




# # # # # 🐣 Notes-Based Practice
# # # # Q1. Class + Object
# # # # Person class banao jisme name aur age ho, aur ek method greet() jo print kare:
# # # # Hello! My name is Umer and I am 22 years old.

# # # class Person:
# # #     def __init__(self,name,age):
# # #         self.name = name
# # #         self.age = age

# # #     def greet(self):
# # #         print(f"Hello! My name is {self.name} and I am {self.age} years old.")


# # # p1 = Person("ali",17)
# # # p1.greet()        


# # # # Q2. State wali class
# # # # Notes mein Person class thi jisme running, walking, sleeping tha — ab tum khud Robot class banao jisme:

# # # # States hon: "Idle", "Working", "Charging"
# # # # Methods: work(), charge(), show_state()


# # # class Robot:
# # #     def __init__(self,name):
# # #         self.name = name
# # #         self.state = "Idle"
        
# # #     def work(self):
# # #         self.state = "Working"
# # #         print(f"{self.name} is now working.")

# # #     def charge(self):
# # #         self.state = "Charging"
# # #         print(f"{self.name} is now charging.")

# # #     def show_state(self):
# # #         print(f"{self.name} is currently in '{self.state}' state.")


# # # r1 = Robot("ali")
# # # r1.work()
# # # r1.charge()
# # # r1.show_state()        


# # # # Q3. Parameterized Constructor
# # # # Car class banao jisme brand, model, color hon constructor mein, aur ek method info() jo print kare:
# # # # Toyota Corolla - White

# # # class Car:
# # #     def __init__(self,brand,model,color):
# # #         self.brand = brand
# # #         self.model = model
# # #         self.color = color

# # #     def info(self):
# # #         print(f"{self.brand} {self.model} - {self.color}")      

# # # c1 = Car("Toyota","Corolla","White")
# # # c1.info()        

# # class Check:
# #     def __init__(self,name,age,profession):
# #         self.name = name
# #         self.age = age
# #         self.profession = profession

# # p1 = Check("ali",17,"student")
# # print(p1.__dict__)












# class Bank:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.__balance = balance

#     def deposit(self,amount):
#         self.__balance += amount
#         return self.__balance


#     def withdraw(self,amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             return self.__balance

#         else:
#             print("insufficient funds")    

            
#     def get_balance(self):
#         return self.__balance

   
# ali = Bank(8452895724895,10)   
# print(ali.deposit(55))
# print(ali.withdraw(60))
# print(ali.get_balance())

    # polymorphm
class Animal:
    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        return "sound"
        

class Dog(Animal):
    def __init__(self,name,age,breed,color):
        super().__init__(name,age,breed)
        self.color = color

    def info(self):
        print("woof woof")  


d1 = Dog("shephars",4,"mix","red")
d1.info()        
        

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
       print("Car stopped")

c1 = Car()
c1.start()     
c1.stop()