###task from lesson about break and continue###
#Task 1
#Write a program that adds 3 even and positive numbers given by the user.
#If the number is negative or odd, the program will ask for the number again. 
#The program is supposed to ask for positive even numbers until it adds 3 numbers.
sum = 0
i = 0

print("Give me 3 even and positive numbers. I will add them.")

while i < 3:
    x = int(input(f"{i+1} number: "))

    if((x < 0) or (x % 2 != 0)):
       print("Wrong number! It was supposed to be a postive AND even number.")
       continue

    sum += x
    i += 1
    print(f"Actual sum: {sum}")