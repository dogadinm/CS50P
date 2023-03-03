i = input('Input: ')
a = 'aAeEiIoOuU'
print('Output: ', end='')

for q in a:
    i = i.replace(q,'')

print(i)