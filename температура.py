c = float(int(input('Введіть занчення в градусах Цельсія: ')))
f = 32+9/5*c
k = c+273.15

print(f'{"{:*^15}".format(f)}{"{0:*^15}".format(k)  }')
