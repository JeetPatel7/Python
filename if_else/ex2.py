weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')


if unit.upper == "L":
    convert = weight * 0.45
    print(f'{convert} in kg')

else:
    convert = weight / 0.45
    print(f'{convert} in pound')


