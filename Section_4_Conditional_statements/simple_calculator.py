###using conditional statement "if"###

choice = input("Simple calculator.\n\
Pick one: * -> multiply, / -> divide + -> add, - -> subtract, ** -> increase, % -> modulo: \n\
I choose: ")

a = int(input("First number: "))
b = int(input("Second number: "))

if(choice == '*'):
    print(a * b)

elif(choice == '/'):
    if(b == 0):
        print("Do not divide by 0!")
    else:
        print(a / b)
elif(choice == '+'):
    print(a + b)
elif(choice == '-'):
    print(a - b)
elif(choice == "**"):
    print(a**b)
elif(choice == '%'):
    print(a%b)
else:
    print("Wrong data! Try again.")