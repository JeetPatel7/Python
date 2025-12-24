
# weight_lbs = input("Enter your weight in pound(lbs): ")

# weight_kg = weight_lbs * 0.45 --> string * float... not possible

# print("Your weight in kg's is:", weight_kg)

# TypeError: can't multiply sequence by non-int of type 'float'


weight_lbs = input("Enter your weight in pound(lbs): ")

weight_kg = float(weight_lbs) * 0.45 

print("Your weight in kg's is:", weight_kg)