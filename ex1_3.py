print('Ведите координаты 2х точек:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
k=(y1-y2)/(x1-x2)
b=y2-k*x2
print(f'Уравнение прямой имеет вид y={k:.2f}x+{b:.2f}')