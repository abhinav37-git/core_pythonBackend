# from math import *
# number =int(input('Input the number '))

# print("The number input is ", number, "Square root of number is ", sqrt(number))

# sentence = input("Enter the sentence: ")

# print("Your sentence is: " + sentence)

# word1 = input("Enter the word to replace: ")

# word2 = input("Enter the word to replace it with: ")

# print(sentence.replace(word1, word2))

# countries = ["India", "Australia", "USA", "New_Country", "Ghana"]
# name = "abhinav"
# age = 21
# print(type(countries), type(name), type(age))

# countries[2] = 5

# print(countries)
# print(type(countries))

# countries[3] = True
# print(type(countries[3]))
# print(len(countries))

# countries = list(("Constructor", 21, False))
# print(type(countries))
# print(countries)


# list1 = [1, 5, 8, 11, 12]
# list2 = ["Apples", "Mangoes", "Bananas", "Orange"]

# del list1[1]

# print(list1)
# list1.sort()
# print(list1)


# list3 = list1.copy()

# print(list3)

# list2.pop(2)
# print(list2)

# list2.remove("Apples")
# print(list2)

# del list2[1]
# print(list2)
# # list1.append(6)
# list1.extend(list2)

# list1.append("Cherry")

# print(list1)

# list2.insert(2, "New_fruit")

# print(list2)

# list2.remove("New_fruit")
# print(list2)

# list2.clear()

# print(list2)

##Tuples
# three_numbers = (1, 2, 3, "Abhinav")
# strings = ("New1", "New2", "New3")
# boo = (True, False, True)

# print(three_numbers)
# print(strings)
# print(boo)
# # print(three_numbers[0])

# # three_numbers[1] = 23
# print(len(three_numbers))
# print(type(three_numbers))

# three_number2 = tuple((1, 2, 3, "Abhinav"))
# print(three_number2)

##functions in python

# def greetings_function(name, age, occupation):
#     print("Welcome new user " + str(name), age, occupation)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# occupation = input("Enter the occupation: ")
# greetings_function(name, age, occupation)

#Return statements in python function

# def my_function():
#     return 5+4

# def add_numbers(num1, num2):
#     print("Hello")
#     return num1+num2

# print(my_function())

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("Addition of numbers is", add_numbers(num1, num2))

# If statements in python

# number = int(input("Enter the number: "))
# if (number%2 == 0):
#     print("Even number")

# else:
#     print("Odd number")

# a="Abhinav"
# b="Abhinav"
# if a == b:
#     print("a is equals to b")
# elif a == 
# else:
#    print("a is not equals to b")

# boy = True
# short = True

# if boy == True and short == False:
#     print("He is a boy or he is short")
# else:
#     print("A is none of the two") 

value = input("Input a string: ")

if type(value) == str:
    print(value + " is a string")

elif type(value) == int:
    print(value, " is an Integer")

else:
    print("A is none of the two")