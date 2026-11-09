# type casting 


# a = int(input("enter your age: "))
# b = int (input("enter your height: "))


# sum = a + b
# print("sum of age and height is: ", sum)


# string function


# x = "hello world"
# print(x.upper())
# print(x.lower())
# print(x.replace("h", "H"))
# print(x.split(" "))
# print(x.find("world"))
# print("s" in x)


# x = int(input("enter a number: "))  
# y = int(input("enter another number: "))
# operator = input("enter an operator (+, -, *, /): ")


# if operator == "+":
#      result = x + y
#      print("result: ", result)
# elif operator == "-":
#      result = x - y
#      print("result: ", result)
# elif operator == "*":
#      result = x * y
#      print("result: ", result)
# elif operator == "/":
#      result = x / y
#      print("result: ", result)




# nums = range(1 , 11 , 2)
# print(nums)
# count = 1
# while count <= 10:
#     for num in nums:
#         print(num * count, end = " ")
#     print()
#     print(count)
#     count += 1
# for num in nums:
#     print(num)
 




# some complex data type




# set , dictionary , list , tuple

# 1 list --> immutable , ordered , allows duplicates

# nums = [33, 44, 55, 66, 77, 88, 99]



# nums.append(100)
# nums.insert(0,22)
# nums.remove(55)
# print("Length of nums:", len(nums))

# print(nums[len(nums) - 1])  # last element
# print(nums[-3:-1])

# for num in nums:
#      print(num)


# tuple --> immutable , ordered , allows duplicates
# tuple1 = ( 2, 3, 4, 5, 6, 7, 8, 9 , 5, 5, 5, 5 ,2 , 1)
# print("Length of tuple1:", len(tuple1))
# print("First element of tuple1:", tuple1[0])
# print(tuple1)


# duplicate value conut
# print("Count of 5 in tuple1:", tuple1.count(5))



# for num in tuple1:
#      print(num)



# set --> mutable , unordered , does not allow duplicates
# set1 = { 2, 3, 4, 5, 6, 7, 8, 9 , 5, 5, 5, 5 , 1}
# set1.union({10, 11, 12})
# set1.add(13)
# set1.remove(3)
# print("Length of set1:", len(set1))
# print(set1)
# set1.discard(423)
# set1.update({10, 11, 12 , 520})
# print(set1)



# dictionary --> mutable , unordered , does not allow duplicates
# dict1 = { "name": "John", "age": 30, "city": "New York", "age": 40}
# print((dict1))
# dict1["age"] = 50000000
# print((dict1))

# for key in dict1:
#     print(key, ":", dict1[key])



# functions

# 1 . user defined function
# 2 . built in function 
# 3 . moduler function 

# from math import random
# print(random)

# def sum(a , b):
#     return a + b 

def numberGuessor():
    import random
    number = random.randint(1, 100)
    guess = None
    # attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != number:
        guess = int(input("Enter your guess: "))
        # attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")