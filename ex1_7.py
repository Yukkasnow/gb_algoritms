def compare(a,b,c):
    if a + b > c and a+c>b and b+c>a:
        print('Треугольник существует')
    else:
        print('Треугольник не существует')

side_1=int(input('Введите первую сторону треугольника'))
side_2=int(input('Введите вторую сторону треугольника'))
side_3=int(input('Введите третью сторону треугольника'))

compare(side_1,side_2,side_3)