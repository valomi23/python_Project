a = int(float(input('Введіть одиницю виміру (метри): ')))
milya = round(a/1609.344, 2)
fut = round(a/0.3048, 2)
dyim = round(a/0.0254, 2)
print(f'Миль: {format(milya)} \nФут: {fut} \nДюйм: {dyim}')





