number = [2,3,2,5,5,3,6,3,5,3,6,8,7,8,6]
unique = []
for numbers in number:
    if numbers not in unique:  # remove duplicates
        unique.append(numbers)

print(unique)        

unique.sort()
print("Sorted list :",unique)
