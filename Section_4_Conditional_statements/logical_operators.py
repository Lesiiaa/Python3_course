###using logical operators###
number = int(input("I will check if the number is in range 1-10: "))

if(number >= 1 and number <= 10):
    print("Yes, number is in this range.")
else:
    print("No, number does not belong to this range.")

number_2 = int(input("I will check if the number is in range 1-10 or 17-20: "))

if((number_2 >= 1 and number_2 <= 10) or (number_2 >= 17 and number_2 <= 20)):
    print("Yes, number belongs to this range.")
else:
    print("No, number does not belong to this range.")