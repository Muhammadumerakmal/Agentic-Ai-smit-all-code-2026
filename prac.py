# Task 1 (Lesson 01–02): Apna ek "bio card" print karo — naam, age, city, aur kya ban'na chahte ho. Sirf print() aur variables use karo.

# my_bio = "my name is umer akmal , my age is 18, i live in karachi and i want to become a full stack web developer"

# print(my_bio)


# Task 2 (Lesson 03): Ek number lo. Agar 18 se zyada hai toh "adult" print karo, agar 13 se zyada hai toh "teen", warna "kid".

# age = 13

# if age >= 18:
#     print("adult🧑")

# else:
#     print("kid👶")    


# Task 3 (Lesson 04): 1 se 10 tak loop chalao. Sirf even numbers print karo.

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# Task 4 (Lesson 05): add(a, b) function banao with type hints — def add(a: int, b: int) -> int. Phir multiply bhi banao.

# def add(a:int,b:int)->int:
#     return a+b

# def multiply(a:int,b:int)->int:
#     return a*b


# print(add(5,9))
# print(multiply(5,9))



# Task 5 (Lesson 06–07): Apni favourite 5 tech skills ki list banao. Phir ek dict banao jisme skill name key ho aur experience (years) value ho.

tech_list = ["js","py","ts","css","html"]

tech_dict = {
    "skill":"full stack dev",
    "exp":3
}

print(tech_list)
print(tech_dict)