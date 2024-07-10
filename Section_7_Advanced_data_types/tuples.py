###trying out tuples###
tuple = (1, 42, 12, -4)
print(tuple[0])

print(len(tuple))
print(max(tuple))
print(1 in tuple)
print('1' in tuple)

for number in tuple:
    print(number)


list = list(tuple)
list.append(4)
print(list)