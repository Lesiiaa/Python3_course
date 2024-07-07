###trying out break and continue###
sum = 0
difference = 100
i = 0

print("Give me 3 positive numbers. I will add them.")

while i < 3:
    x = int(input(f"{i+1} number: "))
    if(x < 0):
        print("It was supposed to be a positive number!")
        continue
    sum += x
    print("Actual sum: ", sum)
    i += 1

message = "\nGive me {} positive numbers. I will subtract them from a 100."
print(message.format(3))

for i in range(3):
    x = int(input(f"{i+1} number: "))
    if(x > 0):
        difference -= x
    else:
        print("It was supposed to be a positive number! I am finishing the program.")
        break
    print(f"Actual difference: {difference}")


