numbers_range=input('Введите числа через пробел').split( )
result_range=[]
max_summ=0
max_n=0
for num in numbers_range:
    summ=0
    for n in num:
        n=int(n)
        summ+=n
    if summ>max_summ:
        max_summ=summ
        max_n=num
    result_range.append(summ)
result_range.sort()
print(f'число с наибольшей суммой цифр: {max_n}\n'
      f'сумма его цифр: {result_range[-1]}')