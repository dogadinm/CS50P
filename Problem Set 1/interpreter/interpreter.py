i = input('What do you want to count ? ')
x, y, z = i.split(' ')

nx = float(x)
nz = float(z)

if y == '+':
    answer = nx + nz

if y == '-':
    answer = nx - nz

if y == '*':
    answer = nx * nz

if y == '/':
    answer = nx / nz

print(round(answer, 1))

