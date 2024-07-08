###creating lists and basic operations on them###
names = ["Julie", "John", "Georgia", "Xaden", "Anika"]
numbers = [1, 54, -2, 20]
mixed = [1, "aa", 54, "m"]

print(names)

for name in names:
    print(name)

print(f"First element: {names[0]}")
print(f"Last element: {names[-1]}")

names[-1] = "Philip"
print(f"Changed last element: {names[-1]}")

print(3 * numbers)
print([4] + numbers)

numbers = [8, 30] + numbers
print(numbers)