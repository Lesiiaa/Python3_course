###creating nested data###
guest_list = [
["Julie", 23, "female"],
["Johnny", 25, "male"],
["Georgia", 17, "female"]
]

guest_list_2 = {
("Olivia", 30, "female"),
("Rick", 70, "male"),
("Morty", 14, "male")
}

guest_list_3 = {
("Rick", 70, "male"),
("Zack", 70, "male"),
("Zeref", 14, "male")
}

print(guest_list[0])
print(guest_list[1][1])

guest_list[0][1] = 29
guest_list.append(["Fabio", 40, "male"])
print(guest_list)


guest_list_4 = guest_list_2 & guest_list_3
print(guest_list_4)

for name, age, sex in guest_list:
    print("Name: ", name)
    print("Wiek: ", age)
    print("Plec: ", sex)
    print("\n")



