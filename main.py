# from requests import get as get_request 

# response = get_request("https://jsonplaceholder.typicode.com/todos")

# print(response.json())


# # math module use karo
# Ek function banao: circle_area(radius: float) -> float
# Formula: pi * r * r
# math.pi use karo — hardcode mat karo 3.14


# import math

# def circle_area(radius:float)->float:
#     return math.pi * radius * radius

# print(circle_area(5))


# # random module use karo
# Ek function banao: random_greeting(names: list) -> str
# list mein se randomly ek naam uthao
# aur return karo: "Hello, Umer! 👋"
# Hint: random.choice()

# import random   

# def random_greeting(names:list)->str:
#     return f"Hello, {random.choice(names)}! 👋"

# print(random_greeting(["Ali","Waqar","Sami"]))




# import prac

# print(prac.eat(2))


# import random


# for _ in range(10):
#     print(random.random())


# def greet():
#     name = "Harry"
#     print(f"Hello, {name}!")
    
# print("Welcome!", name)

# def sum_numbers(a: int, b: int) -> int:
#     sum: int = a + b
#     return sum

    
# result = sum_numbers(5, 10)
# result_1 = sum_numbers(20, 30)
# print(result)
# print(result_1)


# def modify_value(x):
#     x = 10
#     print("Within function:", x)

# # Immutable object (integer)
# x = 5
# print("Original:", x)
# modify_value(x)
# print("After function:", x)

# print("\n")
# print("\n")


# def modify_list(lst):
#     lst.append(4)
#     print("Within function: ", lst, " - ID:", id(lst))

# # Mutable object (list)
# lst = [1, 2, 3]
# print("Original:", lst, " - ID:", id(lst))
# modify_list(lst)
# print("After function:", lst, " - ID:", id(lst))

        # nums: list[int] = [1, 2, 3, 4, 5, 6]

        # def my_nums(a, b, *arg):
        #     print(a)
        #     print(b)
        #     print(arg)
        #     return sum(arg)


        # # print("Sum     = ", my_nums(1,2 ,3,4,5,6),"\n")
        # # print("Sum     = ", my_nums(1,2 ,3),"\n")
        # print("Sum     = ", my_nums(*nums),"\n")


        # # str()
        # # int()
        # # list()
        # # tuple(LIST)

# def greet(name: str = "John") -> str:
#     return f"HI, {name}!"

# greeting = greet("Ali")
# print(greeting)

#! POSITIONAL_ONLY = "/"

# def info(name, age, cnic,  /):
#     pass

# info("Ali", 30, "12345-6789012-3")

#! KEYWORD ONLY = "*"

# def info(name, *, age, cnic):
#     pass

# info("Ali", age=30, cnic="12345-6789012-3")


# def add_two(x, y):
#   return x + y

# my_lambda = lambda x, y:  x + y;

# full_name = lambda first, last: f"{first} {last}"

# print(add_two(1,2))
# print(my_lambda(1,2))
# print(full_name("John", "Doe"))


lambda_func = lambda x, y : x + y

print(lambda_func(5, 10))