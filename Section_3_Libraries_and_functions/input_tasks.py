###tasks from lesson about collecting data from user###
#Task 1
#Create a program that asks the user to enter their name, age, and favorite color.
#Write down values in an eye-pleasing way. Write down how old the user is and how old they will be in a year.
print("Hi! Give me some information so I know more about u!")
name = input("What's your name? -> ")
age = int(input("How old are u? -> "))
colour = input("What's your favorite colour? -> ")

print("\n")
print(f"Hi {name}! Your favorite colour is {colour}.\n\
You are {age} years old.\n\
You will be {age + 1} next year.")