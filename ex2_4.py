n=int(input('Введите длину ряда'))
a=1
i=0
summ=0
while i<n:
    summ=summ+a
    a=a*(-0.5)
    i+=1
print(f'сумма чисел последовательности равна {summ}')