i = input('What is the answer to the Great Question of Life, the Universe and Everything ? ')
if i.strip() == '42' :
    print('yes')

elif i.lower().strip() == 'forty-two':
    print('yes')

elif i.lower().strip() == 'forty two':
    print('yes')
    
else:
    print('no')