###task from lesson about loops - for###
#Task 1
#Write a program that will write numbers divided by 5 and indivisible by 6 from 0 to 200
for i in range(200):
    if(i % 5 == 0 and i % 6 != 0):
        print(i)