###using following functions on lists###
#len(), .append, .extend, .insert(where, what), .index, 
#sort(), max(), min(), .count, .pop, .remove, .clear, .reverse
list_1 = [54, 1, -2, 20, 1]
list_2 = ["Julie", "Finnick"]

list_1.append(4)
print(list_1)

list_1.extend([2,12,3,8])
print(list_1)

print(list_1.index(-2))

list_1.sort()
print(list_1)

list_1.sort(reverse = True)
print(list_1)

print("Max:", max(list_1))

print("How many 1?:",list_1.count(1))

list_1.remove(1)
print(list_1)

list_2.insert(0, "Giorno")
print(list_2)

list_2.reverse()
print(list_2)

list_2.pop()
print(list_2)

list_2.clear()
print(list_2)