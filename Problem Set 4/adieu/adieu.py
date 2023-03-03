import inflect

p = inflect.engine()
list =[]


while True:
    try:
        name = input('Name: ')
        list.append(name)
    except EOFError:
        break
add = p.join(list)

print('Adieu, adieu, to ' + add)