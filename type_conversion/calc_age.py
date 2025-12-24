# birth_year = input("Enter your birth year: ")
# age = 2025 - birth_year --> here it is considering birth_year as an string. int - string....not possible
# print("Your age is", age)

# TypeError: unsupported operand type(s) for -: 'int' and 'str'

birth_year = input("Enter your birth year: ")
print(type(birth_year))

age = 2025 - int(birth_year)
print(type(age))

print("Your age is", age)
