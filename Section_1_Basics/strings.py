###simple operations on strings###
#adding strings
name = "John"
surname = "Smith"

together = name + " " + surname
print(together)

#ways of writing long strings (\,"""")
long_string = "Text about nothing Text about nothing Text about nothing\
Text about nothing Text about nothing Text about nothing Text about\
nothing Text about nothing Text about nothing "
print(long_string)

long_string = """Text about nothing Text about nothing Text about nothing
Text about nothing Text about nothing Text about nothing Text about
nothing Text about nothing Text about nothing """
print(long_string)

#checking if the name is female
name = "Wiola"
last_letter = name[-1]
if last_letter == 'a':
    print(True)
else:
    print(False)

#choosing which elements to print
print(name[:])
print(name[1:3])