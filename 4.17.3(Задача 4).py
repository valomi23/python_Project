a = '1 2 3 4 5'
b = a.split()
c = list(b)
c.reverse()
print(f'{b}\n{c}')
print(''.join(c))