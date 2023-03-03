x = 50
while x > 0:
    print('Amount Due: ', x)
    money = int(input('Insert coin: '))

    if money in [25, 10, 5]:
        x = x - money

change = abs(x)
print('Change owend:', change)