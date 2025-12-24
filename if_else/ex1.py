amount = 1000000

has_good_credit = True
# has_good_credit = False

if has_good_credit:
    down_payment = amount * 0.1
else:
    down_payment = amount * 0.2

print(f'down payment : ${down_payment}')
