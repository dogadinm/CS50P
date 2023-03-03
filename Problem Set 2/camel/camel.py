i = input('Came case: ')
a = 'ABCDEFGHIJKLMNOPQRSTUVXYWZ'
print('Snake case: ', end='')

for q in a:
    i = i.replace(q,'_'+ q)
i = i.lower()
print(i)