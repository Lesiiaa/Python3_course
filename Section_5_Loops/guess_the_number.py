###guess the number - simple game###
import random

number = random.randrange(101)
user_number = -1

print("Hello! Play Guess the Number with me!\n\
I will think of random number in range 0-100 and you have to guess it.\n\
Ready?")

while(number != user_number):
    user_number = int(input("Guess the number: "))

    if((user_number < 0) or (user_number > 100)):
       print("Wrong number! Range 0-100! Try agin!")

    elif(user_number == number):
        print(f"Congrats! You got it! My number was: {number}")

    elif(user_number > number):
        print("Your number is higher than mine! Try agin!")

    else:
        print("Your number is lower than mine! Try again!")