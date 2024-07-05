###task from lesson about loops - while###
#Task 1
#Write a program summing up 4 numbers (data from user)
sum = 0
i = 0

print("Give me 4 numbers to add.")

while(i < 4):
    x = int(input("Number: "))
    sum += x
    i += 1
    
print(f"Sum: {sum}")
