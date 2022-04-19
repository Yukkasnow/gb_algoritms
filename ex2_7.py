n=int(input('Введите n'))
a=1
summ=1
while a!=n:
    summ=summ+(a+1)
    a += 1

b=n*(n+1)/2

if summ==b:
    print('Равенство выполняется')
else:
    print('Равенство не выполняется')