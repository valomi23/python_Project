import sys
import math

x1 = math.radians(float(input('Введіть широту у градусах: ')))
y1 = math.radians(float(input('Введіть довготу у градусах: ')))
x2 = math.radians(float(input('Введіть широту у градусах: ')))
y2 = math.radians(float(input('Введіть довготу у градусах: ')))
rz = 6371.032
vid_km = rz*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print(f'{"{:>10}".format(round(vid_km, 3))}')
