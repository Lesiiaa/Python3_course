#Task 1
#Below is the list of people who have access to secret information:
#names = ["Joseph", "Giorno", "Jonathan"]
#If someone in the 'names' list is specified by the user in the 'name' variable display corresponding message.
names = ["Joseph", "Giorno", "Jonathan"]

print("\nWelcome to our database. Please answer the following question.")
name = input("What is your name? ").capitalize()

if(name in names):
    print("Welcome! You have access to data.")
else:
    print("Access denied.")