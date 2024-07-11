###trying out dictionaries###
rooms = {49:"Julie", 89:"Gregory"}
print(rooms)

rooms[49] = "John"
rooms[50] = "Leila"
print(rooms)

rooms.update({400:"Karen", 500:"Chloe"})
del(rooms[49])
rooms.pop(400)
rooms.popitem()
print(rooms)

print(len(rooms))

a = {"name":"Fifi", "surname":"Paw"}
print(a["name"])
print(a.get("surname"))
